# NYClean

## Inspiration
Those who live in NYC can relate to the fact that NYC is the city of lights but also one of the dirtiest if not the dirtiest cities in America. Our developers live in different boroughs of New York, but share the common problem of walking by **overfilled garbage cans** that can easily tip over and spill if one more coffee cup is placed on top. This problem cause the streets to be extremely dirty and polluted, and it affects the lives of many New Yorkers.

## What it does
We trained IBM Watson's Visual Recognition by giving positive and negative cases, where the positive case is given overflowing garbage cans and negative case is given empty garbage cans. Each cases were given many photos for optimization and accuracy. Our code makes the camera take a picture every second continuously, the pictures are then sent to IBM Watson using the API to get a score of whether the can is full or not. Our code takes the average of every 50 scores and compares that average our threshold. Once a average is above out threshold, we know that the garbage can is full and needs to be cleaned out. The platform will then send a text to 322 using the Twilio API to alert a full garbage can.

## Authentications for API
Make an auth.py file within your local computer, change the api keys for twilio and ibm

## What's next for NYClean
We planned to integrate this application with security cameras near trash bins throughout the city to execute this operation on a bigger scale.
We also aim to implement the same platform on an android app so that users can take pictures of filled garbage cans and have those pictures send to our Trash Identifier. When the threshold that we set is met, we know that the trash is actually full, and it will trigger the Twilio API to alert 311. To give users a incentive to use the app, we have spoken to NYC public data representatives, and unlimited metro cards can be given out to users when they reported a certain amount of full trash cans.
With this app, we hope NYC will become a cleaner and healthier city!

## https://devpost.com/software/nyclean
