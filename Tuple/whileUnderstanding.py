print("Tuple Using While Loop")  
# Print a heading to indicate the start of tuple iteration using a while loop
# ट्युपल वापरून व्हाईल लूपची सुरुवात दर्शविण्यासाठी शीर्षक छापा

While_loop_Tuple = (10, 20, 30, 40, 50)  
# Define a tuple with 5 integer elements; tuples are immutable collections
# ५ पूर्णांक असलेला ट्युपल तयार करा; ट्युपल बदलता येत नाहीत (immutable)

i = 0  
# Initialize index variable i to 0; used to access tuple elements by position
# अनुक्रमणिका i ला ० ने सुरू करा; ट्युपलमधील घटक क्रमाने प्रवेशासाठी वापरली जाते

while i < len(While_loop_Tuple):  
    # Loop while i is less than the length of the tuple (which is 5)
    # Using len() ensures we don’t access indexes outside the tuple, avoiding errors
    # लूप चालवा जोपर्यंत i ट्युपलच्या लांबीपेक्षा कमी आहे (येथे ५)
    # len() वापरल्याने आपण चुकीचे अनुक्रमांक वापरण्यापासून वाचतो

    print(While_loop_Tuple[i])  
    # Print the element at the current index i
    # सध्याच्या i अनुक्रमांकावरील घटक छापा

    i += 1  
    # Increment i by 1 to move to the next element in the next loop iteration
    # i ची किंमत १ ने वाढवा जेणेकरून पुढील लूपमध्ये पुढील घटक मिळेल

print("End of an Application")  
# After the loop finishes, print this message to indicate the program finished iterating
# लूप पूर्ण झाल्यानंतर हा मेसेज छापा की प्रोग्रॅम संपला

print("--------------------------------------------------")  
# Print a separator line for clarity between sections of output
# वेगळ्या भागांमध्ये स्पष्टता राखण्यासाठी विभाजक ओळ छापा


# Second while loop starts here
while i < 3:  
    # Loop while i is less than 3
    # Note: 'i' is currently 5 after the first loop, so this loop **will not run** because 5 < 3 is False
    # i ची किंमत ३ पेक्षा कमी असल्यास लूप चालवा
    # लक्षात घ्या: पहिल्या लूपनंतर i ची किंमत ५ आहे, म्हणून हा लूप चालणार नाही कारण ५ < ३ चुकीचे आहे

    print(While_loop_Tuple)  
    # Print the entire tuple (not individual elements) during each iteration of the loop
    # प्रत्येक लूपमध्ये संपूर्ण ट्युपल छापा (वैयक्तिक घटक नाही)

    i += 1  
    # Increment i by 1 (though this won't be executed in this case since loop doesn't run)
    # i ची किंमत १ ने वाढवा (पण हा कोड येथे चालणार नाही कारण लूपच सुरु होत नाही)

print("End of an Application")  
# Print message indicating the end of the second loop/application
# दुसऱ्या लूप/प्रोग्रॅमच्या समाप्तीची माहिती देणारा मेसेज छापा
