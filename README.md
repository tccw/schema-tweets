Follow the account [@claudeglasses](https://twitter.com/claudeglasses)

**SCHEMA-tweets** is a tiny script designed to run as a cron job. 
It's only purpose is to post triptychs of landscape photos generated
with Nvidia's [styleGAN2](https://github.com/NVlabs/stylegan2).

The concept is inspired by Alexander Gronsky's [SCHEMA](https://www.alexandergronsky.com/)
which focuses on repetition in urban spaces. My images take this idea to the world of landscape
photography, creating three images with small variations. Are they the same scene at 
different times? Different but very similar landscapes? With a GAN model they can be either.

These images were trained off of a set of  ~4000 "mountain landscapes"
scraped from Flickr<sup>[1]</sup>, taking advantage of transfer learning from Nvidia's 
pre-trained 256x256 churches model (stylegan2-church-config-f).

More information and a walk-through of the training, generating, and ranking used to determine 
the post order of the images will follow soon.


<sup>[1]</sup> Photos with licenses 1, 2, 4, 5, 7, 8, 9, 10 [[id codes here](https://www.flickr.com/services/api/flickr.photos.licenses.getInfo.html)]