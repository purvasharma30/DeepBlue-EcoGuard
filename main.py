import streamlit as st
import app
import app2
import rule_based_classifier as rbc
from inference import garbage
import seaborn as sns
import matplotlib.pyplot as plt

# Define waste labels for the project
labels = ['Mask', 'can', 'cellphone', 'electronics', 'gbottle', 'glove', 'metal', 'misc', 'net', 'pbag', 'pbottle',
          'plastic', 'rod', 'sunglasses', 'tire']

# Main function to create the Streamlit app
def main():

    # Set up the sidebar navigation
    st.sidebar.title('Navigation')
    selected_model = st.sidebar.selectbox('', ['Home', 'Underwater Waste Detection Model',
                                               'Water Quality Assessment Model',
                                               'Water Potability Test Model', 'Generated Report'])
    # display appropriate content based on selected model
    if selected_model == 'Home':
        st.title('DeepBlue EcoGuard')
        st.image('./assets/yacht.jpg')
        st.success('DeepBlue EcoGuard tackles the rising issue of underwater waste with three key solutions: a YoloV8  '
                   'Algorithm for precise waste detection, a rule-based classifier for assessing aquatic habitat, and a '
                   'Machine Learning model to classify water quality. The YoloV8 Algorithm, trained on 5000 images, detects '
                   'waste, while the rule-based classifier uses guidelines from the US EPA and WHO for habitat assessment. '
                   'The Machine Learning model, trained on a dataset of over 6 million rows, reliably classifies water as fit or '
                   'unfit. This project offers a comprehensive approach to safeguard our oceans and marine life.'
                   )
    elif selected_model == 'Underwater Waste Detection Model':
        app.app()
    elif selected_model == 'Water Quality Assessment Model':
        rbc.rbc()
    elif selected_model == 'Water Potability Test Model':
        app2.app2()
    elif selected_model == 'Generated Report':
        st.header('Frequency of all the waste labels')
        occurrences = [garbage.count(labels[i]) for i in range(len(labels))]
        sns.barplot(y=labels, x=occurrences)
        plt.xlabel("Occurrences")
        plt.ylabel("Labels")
        plt.title("Histogram of Occurrences")
        st.pyplot()


        st.header('Water Quality for Aquatic Life Habitat')
        quality_aquatic = rbc.quality_aquatic
        counts = [quality_aquatic.count(0), quality_aquatic.count(1)]
        if len(quality_aquatic) ==  0:
            st.error("Please run some inference on water quality for aquatic life habitat")
        else:
            ans = max(set(quality_aquatic), key=quality_aquatic.count)
            labels_h = ['Habitual', 'Not Habitual']
            habitual = labels_h[ans]
            colors = ['#cfaca4', '#623337']
            sns.set_style("whitegrid")
            plt.figure(figsize=(6, 6))
            plt.pie(counts, labels=labels_h, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.title('Proportions Of Water Quality')
            st.pyplot()


        st.header('Water Quality for Potability')
        data = app2.quality
        counts = [data.count(0), data.count(1)]
        if len(data) == 0:
            st.error("Please run some inference on water quality assessment")
        else:
            ans = max(set(data), key=data.count)
            labels_wqa = ['Fit for use', 'Polluted']
            qwa = labels_wqa[ans]
            colors = ['#1f77b4', '#ff7f0e']
            sns.set_style("whitegrid")
            plt.figure(figsize=(6, 6))
            plt.pie(counts, labels=labels_wqa, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.title('Proportions Of Water Quality')
            st.pyplot()
            st.header("Conclusion: ")
            st.success(
                f'In the recent images, the most seen type of waste is'
                f' {labels[occurrences.index(max(occurrences))]} that has been seen {max(occurrences)} times.'
                f' Also, the water quality has been analyzed and the water has been labelled as {habitual} for aquatic life'
                f' and {qwa} by humans.'
            )
    else:
        st.warning('Please select a model from the sidebar.')

main()
