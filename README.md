# Objects-in-binary-mask
A Program to count number of objects in binray mask image (like test.png)

# Algorithm
This is the approach implemented in the [main.py](https://github.com/AnikaitSahota/Objects-in-binary-mask/blob/master/main.py).
```
Step 1: Traverse through the image matrix.

Step 2: Occurrence of white pixels shows a new object is found. Hence increment the object counter.

Step 3: To make sure white pixels associated with the same object (i.e., already counter object) is not counter again. We will follow the sub-steps.

      Step 3a: move in four valid direction (i.e., up, down, left, right) from the first white pixel’s occurrence (for every new object).

      Step 3b: for every consecutive white pixel, darken it. And follow step 3a until dark pixels are encountered.

Step 4: Continue the traversal mentioned in step 1. Until you have reached to end pixel of image (in terms of both columns and rows).

Step 5: The object counter shows the number of white object present in a black background.
```
