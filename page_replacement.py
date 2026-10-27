"""
Operating Systems Lab Assignment
Page Replacement Algorithm Simulator
Algorithms: FIFO, LRU, Optimal

Run:
    python page_replacement.py

Enter a page reference string separated by spaces or commas, then enter
the number of frames.
"""

def parse_reference_string(raw):
    """Convert comma- or space-separated page references to integers."""
    parts = raw.replace(",", " ").split()
    if not parts:
        raise ValueError("Please enter at least one page number.")

    try:
        return [int(part) for part in parts]
    except ValueError:
        raise ValueError("Invalid reference string. Use numeric page values only.")


def get_user_input():
    """Read and validate the page reference string and frame count."""
    pages = parse_reference_string(
        input("Enter page reference string (spaces or commas): ")
    )

    try:
        num_frames = int(input("Enter number of frames: "))
    except ValueError:
        raise ValueError("Invalid frame count. Enter a whole number.")

    if num_frames < 1:
        raise ValueError("Number of frames must be at least 1.")

    return pages, num_frames


def fifo(reference, num_frames):
    """FIFO replaces the page that entered memory earliest."""
    frames = []
    next_to_replace = 0
    faults = hits = 0
    trace = []

    for step, page in enumerate(reference, start=1):
        replaced = "-"
        if page in frames:
            status = "Hit"
            hits += 1
        else:
            status = "Fault"
            faults += 1

            if len(frames) < num_frames:
                frames.append(page)
            else:
                replaced = frames[next_to_replace]
                frames[next_to_replace] = page
                next_to_replace = (next_to_replace + 1) % num_frames

        trace.append({
            "Step": step,
            "Page": page,
            "Frames": frames.copy(),
            "Status": status,
            "Replaced": replaced,
        })

    return faults, hits, trace


def lru(reference, num_frames):
    """LRU replaces the page least recently used in the past."""
    frames = []
    last_used = {}
    faults = hits = 0
    trace = []

    for step, page in enumerate(reference, start=1):
        replaced = "-"
        if page in frames:
            status = "Hit"
            hits += 1
        else:
            status = "Fault"
            faults += 1

            if len(frames) < num_frames:
                frames.append(page)
            else:
                victim = min(frames, key=lambda p: last_used[p])
                replaced = victim
                frames[frames.index(victim)] = page

        last_used[page] = step
        trace.append({
            "Step": step,
            "Page": page,
            "Frames": frames.copy(),
            "Status": status,
            "Replaced": replaced,
        })

    return faults, hits, trace


def optimal(reference, num_frames):
    """Optimal replaces the page used farthest in the future.

    If multiple pages are never used again, replace the one that appears
    first in the frame list, as required by the assignment.
    """
    frames = []
    faults = hits = 0
    trace = []

    for index, page in enumerate(reference):
        replaced = "-"
        if page in frames:
            status = "Hit"
            hits += 1
        else:
            status = "Fault"
            faults += 1

            if len(frames) < num_frames:
                frames.append(page)
            else:
                future = reference[index + 1:]
                next_use = {}

                for frame_page in frames:
                    try:
                        next_use[frame_page] = future.index(frame_page)
                    except ValueError:
                        next_use[frame_page] = float("inf")

                farthest = max(next_use.values())
                # This preserves first-in-frames tie-breaking.
                victim = next(p for p in frames if next_use[p] == farthest)
                replaced = victim
                frames[frames.index(victim)] = page

        trace.append({
            "Step": index + 1,
            "Page": page,
            "Frames": frames.copy(),
            "Status": status,
            "Replaced": replaced,
        })

    return faults, hits, trace


def show_trace(name, faults, hits, trace, total_pages):
    """Print the step-by-step trace and algorithm metrics."""
    print("\n" + "=" * 78)
    print(name)
    print("=" * 78)
    print(f"{'Step':<6}{'Page':<8}{'Frame contents':<28}{'Result':<10}{'Replaced':<10}")
    print("-" * 78)

    for row in trace:
        frame_text = "[" + ", ".join(map(str, row["Frames"])) + "]"
        print(
            f"{row['Step']:<6}{row['Page']:<8}{frame_text:<28}"
            f"{row['Status']:<10}{str(row['Replaced']):<10}"
        )

    hit_ratio = hits / total_pages if total_pages else 0
    fault_ratio = faults / total_pages if total_pages else 0
    print("-" * 78)
    print(f"Total page faults : {faults}")
    print(f"Total page hits   : {hits}")
    print(f"Hit ratio         : {hit_ratio:.2%}")
    print(f"Fault ratio       : {fault_ratio:.2%}")


def run_all_algorithms(reference, num_frames):
    """Run all algorithms on the same input and print a comparison."""
    if not reference:
        raise ValueError("Reference string must not be empty.")
    if num_frames < 1:
        raise ValueError("Number of frames must be at least 1.")

    results = {}
    algorithms = [
        ("FIFO", fifo),
        ("LRU", lru),
        ("Optimal", optimal),
    ]

    for name, algorithm in algorithms:
        faults, hits, trace = algorithm(reference, num_frames)
        results[name] = {
            "faults": faults,
            "hits": hits,
            "hit_ratio": hits / len(reference),
            "fault_ratio": faults / len(reference),
            "trace": trace,
        }
        show_trace(name, faults, hits, trace, len(reference))

    print("\n" + "=" * 78)
    print("FINAL COMPARISON")
    print("=" * 78)
    print(f"{'Algorithm':<12}{'Faults':<10}{'Hits':<10}{'Hit ratio':<14}{'Fault ratio':<14}")
    print("-" * 60)

    for name in ("FIFO", "LRU", "Optimal"):
        result = results[name]
        print(
            f"{name:<12}{result['faults']:<10}{result['hits']:<10}"
            f"{result['hit_ratio']:<14.2%}{result['fault_ratio']:<14.2%}"
        )

    return results


def main():
    try:
        reference, num_frames = get_user_input()
        run_all_algorithms(reference, num_frames)
    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
