<h2><a id="Fuel__Management_0"></a>Fuel Transactions - Management</h2>
<p>Practical Python and Data-Centric Development Milestone Project</p>
<hr>
<p>This project is about a website where people can manually enter their fuel transactions receipts. A navigation bar allows moving from three different sections: A "Fuel Transactions" screen shows all captured transactions, "Add Receipts" to capture transaction's information and "Manage Sites" to adding fueling facilities to the database.<br>
>
This is a MongoDB-backed Flask project that allows users to store and manipulate data records.<br>
A Database with several collections has been created with data for "Receipts", "Sites", "Employees", "Pumps" and "Vehicles".
 
The "Add Receipts" screen will cross reference the vehicle ID entered against the MongoDB and will display an error message if the vehicle does not exist.</p>
<h2><a id="UX_9"></a>UX</h2>
<p>My goal in the design of this project was to get people a friendly and easy application to capture all of their fueling transactions receipts and be able to store data about their fueling sites, pumps, employees and vehicle's fleet.</p>
<p>A live demo can be found <a href="https://dashboard.heroku.com/apps/fuel-transactions-management/deploy/github">here</a></p>
<h2><a id="Technologies_16"></a>Technologies</h2>
<p>HTML and CSS<br>
Structure: Materialize <br>
Version control: Git & GitHub<br>
Programming languages: Javascript and Phyton<br>
Deployment: Heroku hosting platform
<h2><a id="Features_22"></a>Features</h2>
<p>Website with functionality for users to create, locate, display, edit and delete records (CRUD functionality).<br>

<p>Features Left to Implement:<br>
I would like to add in the future, screens for adding employees and vehicles to the database as well as reporting capabilities .</p>
<h2><a id="Testing_32"></a>Testing</h2>
<p>I have run diferent testing with all screens making sure they all are responsive and all buttons work correctly. I have verified the integrity of the data from the front end application and the MongoDB database.</p>
<p>This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox) and on multiple mobile devices to ensure compatibility and responsiveness.</p>
<p>During the testing phase, the "Datapicker" function was not working properly. 
Fixed this by adding javascript code to correct a "Materialize" version error.</p>
<h2><a id="Deployment_47"></a>Deployment</h2>
<p>Heroku hosting platform.<br>
The deployed site will update automatically upon new commits to the Github master branch.<br>

<h2><a id="Credits_56"></a>Credits</h2>
<p>Website design idea from Mini Project | Putting It All Together "Task Manager" Code Institute</p>
<h2><a id="Content_60"></a>Content</h2>
<p>Website Fuel Management data samples from "MegaTrak" Automated Fuel Management System. www.megatrak.com</p>

<h2><a id="Acknowledgements_69"></a>Acknowledgements</h2>
<p>The “Navbar” feature was found in MaterializeCSS.com <a href="https://materializecss.com/navbar.html/">Click here</a></p>

<p>This is for educational use.</p>

</body></html>