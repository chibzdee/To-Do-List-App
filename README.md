# To-Do-List-App
A simple to-do list app, made with python, html, css and sqlalchemy as the database

The setup:
Homepage-:
  The homepage was built with html, its a simple table that displays all the to-do's(if-any) and then below it is a form,
  that collects the information that is to be displayed on the table.

The Styling-:
  The app is styled with CSS(cascading style sheet), centering the table and the form and adding colors,
  padding and margins to make it look more appealing to the eye.

The server-:
  The server is built up on a light-weight web framework in python named Flask.
  Within the flask file, functins are written that renders the pages of the application using the route decorator to 
  direct the urls to which particular page is to be shown on the screen.

  The server is also linked with a database model called SQLALCHEMY.
  It is where each task is stored and retrieved from.

  After the data has been  entered into the form, a POST request is sent to the database to store the to-do task that was just entered and
  submitted by the form, and a GET request is used to display all the data that is available in the database.

  An edit and a delete functionality was added to the app in order for users to either change a particular task item or remove it       completely from the table.
  This is done by retrieving the particular item by its "id" which is a unique number given to all database entries (pieces of data).
