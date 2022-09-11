# Devpost-Funathon2022 _ Project **Recyclable**

## Try it Out 
Clone [project repository](https://github.com/phyulwin/Devpost-Funathon2022) locally and open the project folder in your IDE. Install required Python modules and run `main.py` in your IDE. Open your browser and access the development server at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

# Project Story
### about the project
I decided to clean my room the other day, and uncovered bags of random objects and small items that were lost within the piles. Along the way, I picked up draw-string bags from spontaneous events, Amazon package bags, and cups and bottles from small businesses advertising their companies. Amidst the junk, they all seemed to be made of some kind of plastic and I questioned if they were recyclable. Yet, having no resource to directly find the object, I casually threw the rest of it in the trash with a slight hint of guilt that washed away in seconds.

According to the World Bank, an average of 2.01 billion tons of waste is produced every year, with over 33% of it managed in an environmentally unsafe way. The average person can create up to 0.74 kilograms of waste, though it ranges as high as 4.5 kilograms. This is especially prevalent in high-income countries, where just 16 percent of the world's population generates 34% of the earth's waste, equivalent to 683 million tons. If this projection continues, daily per capita waste generation is predicted to increase by 19% by 2050. Though there are existing infrastructures and systems to encourage people to recycle what they can, most do not have clear information on specific instructions, which leads to a failure in utilizing those systems. Thus, our project aimed to create an application that will help people identify what they can recycle within their immediate surroundings, along with simple instructions on where to do so. With a specialized app that will be accessible on the web, people will be able to find and scan objects around them and effectively recycle, reducing global waste by a significant amount.

## What it does
The Object Recyclable is a project that aims to help people recycle their waste by detecting objects in a web camera image and giving information about how to recycle it. Users will hold the object up for a scan, where the website will then load various tabs of instructions on the side. This includes specific statistics on the object's waste impact on the environment, sectioned articles that explain ways to possibly reuse the object, and a map to show recycling sites. Users will be able to use the sorted data to find the best way for them to recycle.

## How we built it
The website was developed using Python, OpenCV, and the Earth911 API. It was designed using the Flask framework. ....

## Challenges we ran into
Initially, during our app development process, we couldn't configure IP Location API and Google Maps Autocomplete Plus API to retrieve the user's location so that we could suggest nearby recycling centers. We concluded that the case might be due to user's IP address being restricted from access for privacy concerns. Hence, we hard-coded the feature without utilizing the APIs for the app prototype. As included in `api_queries.py`, we also learned the idea of building that feature using APIs. 

## Accomplishments that we're proud of

## What we learned
We learned about utilizing OpenCV as a main way to detect objects in images, and experimented with applying masks and contours to categorize shapes. We also learned about several concepts in Machine Learning such as neural networks, the different types of learning, and combining its outputs with our design. We used APIs like Earth911 to request information from datasets, along with web scraping articles and website links to lay out on the application. 

## What's next for Object Recyclable
Following the development of the application, the first improvement would be to develop a custom Machine Learning model to expand the number of items to detect, as well as refine the accuracy of the detection weights. We can add a larger series of reference pictures into a dataset, allowing the application to more accurately label the scanned image. Furthermore, aside from the common objects that the app can detect now, we can also detect text on the objects such as brands, the materials, and manufacturer to give more detailed instructions on its recyclability to minimize pollution and resource use.
