Exercise: Getting Started with Bootstrap

Objectives and Outcomes

This exercise introduces you to the basic features and some classes of Bootstrap. At the end of this exercise, you will be able to:

Understand how to set up a web project to use Bootstrap
Include the Bootstrap CSS and JS classes into a web page
Design a web page structure using a few basic Bootstrap classes
Note: Please remember to retain the folder and all the files that you create in this exercise. Further exercises will build upon the files that you create in this exercise. DO NOT DELETE the files at the end of the exercise.

Setting up the Project Folder

Go to a convenient folder on your computer and create a folder named conFusion. This will be the name of the project that we will implement in the set of exercises to follow.
Downloading Bootstrap

Go to the Bootstrap website http://getbootstrap.com and click on the download button to download the zip file containing Bootstrap files.
Move the bootstrap-3.3.5-dist.zip file to the conFusion folder you created above and unzip it. You should now see a folder named bootstrap-3.3.5-dist. Go to this folder and move the three folders there (css, fonts and js) to conFusion folder above. You can now delete the zip file and bootstrap-3.3.5-dist folder. Now you are all set to use Bootstrap to design your web project.
Download index.html file

Download index.html file to the conFusion folder. This is your starting web page for the project. We have already created the web page with some content to get you started. We will use Bootstrap to style this web page, and learn Bootstrap features, classes and components along the way.
Getting your Web page Bootstrap ready

Open the index.html file in your favourite text editor. If you are using Brackets, you can open the conFusion folder from within Brackets and then open the index.html file as a working file. You can do the same with Sublime Text and some other text editors too.
Open the index.html file in your favourite browser so that you can preview the formatted web page in the browser. If you are using Brackets, you can use the Live Preview button to load and automatically refresh the page in Chrome as you edit the files. A similar set up can be done with Sublime Text after installing some plug-ins.
Insert the following code in the head of index.html file before the title.
    
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head 
         content must come *after* these tags -->
    
Add the following code in the head after the title. This will include Bootstrap CSS into your web page.
        <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/bootstrap-theme.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
Note the subtle change in the fonts of the content of the web page. This is the Bootstrap typography effect coming into play. The default Bootstrap typography sets the font to Helvetica Neue and selects the appropriate font size based on the choice of the heading style and paragraph style for the content.
At the bottom of the page, just before the end of the body tag, add the following code to include the JQuery library and Bootstrap's Javascript plugins. Bootstrap by default uses the JQuery Javascript library for its Javascript plugins. Hence the need to include JQuery library in the web page.
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>

Using a Container class

We use the container class to keep content within a fixed width on the screen, determined by the size of the screen. The alternative is to use the container-fluid class to make the content automatically to span the full width of the screen. We will discuss further about this when we discuss the Bootstrap grid system in the next lecture. Add the container class to the top most div in the file as follows.
<div class="container"> ...
Dividing the content into rows

Let us now add the class row to the first-level inner div elements inside the container. This organizes the page into rows of content. In the next exercise, we will see how we can add other classes to the rows.
    <div class="row"> ...

Creating a Jumbotron

Let us add the class jumbotron to the header class as shown below. This turns the header element into a Bootstrap component named Jumbotron. A jumbotron is used to showcase key content on a website. In this case we are using it to highlight the name of the restaurant.
        <header class="jumbotron"> ... 
In the header add a container class to the first inner div and a row class to the second inner div.
Creating a footer

Finally, in the footer add a container class to the first inner div and a row class to the second inner div.
Conclusion

We have now understood how to set up a web project to use Bootstrap. In the next lecture, we will explore further on responsive design and Bootstrap's grid system.