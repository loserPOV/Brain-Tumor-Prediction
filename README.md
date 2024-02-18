>**Objective**: This project aims to develop a tool for the early detection and classification of brain
tumors using computer vision techniques. Leveraging the power of machine learning and deep learning
algorithms, the system will analyze medical imaging data, particularly MRI scans, to identify the presence of
tumors. The primary objective is to assist radiologists and medical professionals in making faster and more
accurate diagnoses, potentially leading to improved patient outcomes.

>**Technology / Tools**: Python, Pandas, NumPy, Seaborn, Matplotlib, Scikit-Learn, Imblearn, Feature-Engine,
Streamlit, HuggingFace, os, glob, PIL, TensorFlow.

>**Dataset**: https://www.kaggle.com/datasets/preetviradiya/brian-tumor-dataset

>**Results**: 

    1. EDA:

    - The distribution of data shows Brain Tumor (55%) is more prevalent than Healthy (45%), but the dataset is not considered imbalanced as the percentage difference is relatively small.

    - The images in the dataset have not undergone data augmentation, evident from the varying shapes of the images.

    2. Model:

    - The best model architecture is the 'model_base' which uses a sequential architecture without max pooling. However, due to its large size and the high computational cost required, this model will not be used for inference and deployment.

    - The chosen model is the second-best, 'model_seq', an improved version of 'model_base'. Despite 'model_base' having better metric values, 'model_seq' is preferred due to its significantly smaller size.

    - The metrics obtained for 'model_seq' are loss: 0.4077 - precision_1: 0.9057, based on 21 epochs or iterations of training.

    3. Evaluation:

    - The model evaluation results, using precision, recall, and f1-score metrics for two-class classification (0 (Brain Tumor) and 1 (Healthy)).

    - For class 0, precision is 0.75, recall is 0.95, and f1-score is 0.84 with a support of 236 data points. This indicates the model has good precision in identifying class 0 and a high recall rate, meaning it excels in recognizing class 0.

    - For class 1, precision is 0.92, recall is 0.64, and f1-score is 0.76 with a support of 208 data points. This shows the model has very good precision in identifying class 1 but a lower recall, suggesting the model might more often miss data from class 1.

    - Overall, the model accuracy is 0.81, indicating good overall performance. However, it's noted that class 0 performs better than class 1.

>**Deployment**: you can try the deployed model here -> https://huggingface.co/spaces/LoserPOV/Brain_Tumor_Prediction
