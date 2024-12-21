**Dithered quantization** problem (quantizing after adding random noise, i.e. halftoning)  

**Regular Quantization** 
The image quality drops due to the loss of information by quantizing the pixel values  

**Random noise improves the visual quality of images**:  
The image quality perceptually improves with increasing variance. This is because for pixel values close to the threshold of 127, adding variance results in more randomness of the intensities within that particular colocalized region. Because pixels are randomly set to the opposite color of what they would be set to in quantization without noise, they still follow the distribution of intensities but are more mixed together. This results in a gradient-like effect, known as half-toning, which improves the perceptual-visuals.   