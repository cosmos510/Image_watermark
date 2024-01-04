# Image Watermarking App

The Image Watermarking App is a Python project that allows you to add a custom watermark(logo or text) to an image file and save it to the chosen directory. It uses Tkinter, Pillow to create a GUI and implement all the features.

## GUI Layout

The app's GUI consists of several components, including buttons, scales, spinboxes, and option menus, which allow you to adjust the watermark's position, rotation, font size, font type, opacity, and color.
The layout is shown in the following image:

<img width="1448" alt="Screenshot 2024-01-04 at 14 45 58" src="https://github.com/cosmos510/Image_watermark/assets/149656366/c9f647fa-39d5-438e-ae10-018f7ed775c3">

## Image File Selection

The "Select file" button opens a new window, where you can choose any of the jpeg, .jpg, .jpeg, png, .png, bitmap, bmp, gif, .gif files to load. Once the image is loaded, you can add your custom watermark to it.

<img width="1448" alt="Screenshot 2024-01-04 at 14 48 17" src="https://github.com/cosmos510/Image_watermark/assets/149656366/acf915dc-4e73-4469-83e6-d35dec32c17c">

## Watermark Customization
### Text
The app allows you to customize the watermark by providing text that will get transformed into a custom watermark. You can adjust the watermark's position, font size, font type, opacity, and color using the various components in the GUI.
### Logo
The app allows you to customize the watermark logo by providing an image, You can adjust the logo's positionand logo's size using the various components in the GUI.

<img width="1448" alt="Screenshot 2024-01-04 at 14 54 03" src="https://github.com/cosmos510/Image_watermark/assets/149656366/10ddb482-cb9f-4f47-9a78-fbe6b7bc5202">

## Saving Process
Once you have customized your watermark, you can save the watermarked image by clicking the "Save" button. This allows you to name your watermarked image and save it in the chosen file path. The app automatically converts the image file into RGB before saving it.
