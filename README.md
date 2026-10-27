# Page Replacement Algorithm Simulator

An Operating Systems Lab project implemented in Python to simulate three page replacement algorithms: FIFO, LRU, and Optimal.

## Features

- Accepts a page reference string and number of frames.
- Displays step-by-step frame contents.
- Identifies page hits and page faults.
- Calculates hit ratio and fault ratio.
- Compares all three algorithms.
- Includes manual tracing and Belady's anomaly experiments.

## Algorithms

### 1. FIFO (First-In, First-Out)
Replaces the page that has been in memory the longest.

### 2. LRU (Least Recently Used)
Replaces the page that has not been used for the longest time in the past.

### 3. Optimal Page Replacement
Replaces the page whose next use is farthest in the future. It is mainly used as a theoretical benchmark.

## Technologies Used

- Python
- Google Colab / Jupyter Notebook
- GitHub

## How to Run

### Google Colab
1. Open Google Colab.
2. Upload `Page_Replacement_Simulator.ipynb`.
3. Run all cells from top to bottom.
4. Enter the page reference string.
5. Enter the number of frames.
6. Review the output and comparison table.

### Python Source Code

Run the following command in your terminal:

    python page_replacement.py

## Sample Input

    Reference string: 1 2 3 1 4 2 5
    Number of frames: 3

## Performance Metrics

- **Page Faults:** Number of references to pages not currently in memory.
- **Page Hits:** Number of references to pages already in memory.
- **Hit Ratio:** Page Hits / Total Page References.
- **Fault Ratio:** Page Faults / Total Page References.

## Project Files

- `Page_Replacement_Simulator.ipynb` — Google Colab notebook
- `page_replacement.py` — Python source code
- `Page_Replacement_Project_Report.pdf` — Project report
- `README.md` — Project documentation

## Learning Outcomes

- Understand virtual memory and page replacement.
- Implement FIFO, LRU, and Optimal algorithms.
- Compare page replacement performance.
- Study Belady's anomaly.

## Author

- **Name:** Your Name
- **Roll Number:** Your Roll Number
- **Course:** Operating Systems Lab
- **Institution:** Your College Name

## References

- Operating Systems Lab Assignment: Page Replacement Algorithm Simulator.
- Course notes on virtual memory and page replacement.

---

Update your details and add actual execution screenshots before submitting.
