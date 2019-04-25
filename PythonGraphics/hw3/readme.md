## HW 3
The purpose of this homework is to have you do on paper the math/algorithms that you’ll need
to implement for Lab 3, especially Functions 6–10 respectively.
For all of the problems that follow, if you need to use pixel values outside of the given images,
use 0 padding, i.e., assume pixel values of 0 for all pixels outside the images. For questions 1-4,
round to the nearest integer value. For question 5, round to one decimal point.

1. What is the result of 3×3 mean filtering (averaging pixels with their 8-connected neighbors)
for the following image?
        
      ![](images/1.png)

2. What is the result of median filtering (using 8-connected neighbors) for the following image?

    ![](images/2.png)

3. Spatially filter (convolve) the image on the left with the 3 x 3 mask (kernel) shown.

      ![](images/3.png)

4. What is the result of unsharp masking using an A = 1 (a 5 in the center) mask?

     ![](images/4.png)

5. This question walks through the computational steps for gradient-magnitude edge detection
for the following image: (For this question, don’t worry about the border pixels.)
    
    ![](images/5.png)
