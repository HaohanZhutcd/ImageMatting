% Bayesian Matting with Orchard-Boumann Clustering
% Group - Atomic Reactors

% Reading image
img = imread("Images\imagefortesting\input_training_lowres\GT01.png");

% Reading trimap 
trimap = imread("Images\imagefortesting\trimap_training_lowres\Trimap1\GT01.png");

gt_image = imread("Images\imagefortesting\gt_training_lowres\GT01.png");
% Converting both image files to double
img = im2double(img);
trimap = im2double(trimap);

img_obj = initializeVariable();
% Starting timer here
tic;
% Performing Bayesian Matting here
a = getBayesianMatte(img, trimap, img_obj);
% % Generate composite image here
% newB = imread("Images\bear\background.jpg");
% newB = im2double(newB);
% %newB = imresize(newB, [282 420]);
% %composite_img = generateCompositeImage(Fground, newB, alpha_val);
% % Ending timer here
% toc;
% 
% % Displaying Original Image
% figure(1);
% imshow(img);
% title('Original Image');
%  
% % Displaying Alpha Matte
% figure(2);
% imshow(alpha_val);
% title('Alpha Matte');
% shg; hold on;
% 
% % Calculating MSE
% MSE_val = getMSE(alpha_val, gt_image);
% disp(MSE_val);
% % figure(3);
% % imshow(composite_img);
% % title('Composite Image');




