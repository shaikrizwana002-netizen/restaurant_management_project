<!DOCTYPE html>
<html>
<head>
  <title>Contact Us</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">

  <h2 style="text-align: center; color: #333;">Contact Us</h2>

  <form style="max-width: 600px; margin: auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
    <label for="name" style="display: block; margin-bottom: 8px;">Name:</label>
    <input type="text" id="name" name="name" style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;">

    <label for="email" style="display: block; margin-bottom: 8px;">Email:</label>
    <input type="email" id="email" name="email" style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;">

    <label for="message" style="display: block; margin-bottom: 8px;">Message:</label>
    <textarea id="message" name="message" rows="5" style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px;"></textarea>

    <button type="submit" style="margin-top: 15px; background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>
  </form>

</body>
</html>

body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  padding: 20px;
}

h2 {
  text-align: center;
  color: #333;
}

form {
  max-width: 600px;
  margin: auto;
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

label {
  display: block;
  margin-bottom: 8px;
}

input, textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

<!DOCTYPE html>
<html>
<head>
  <title>Contact Us</title>
  <link rel="stylesheet" href="contact.css">
</head>
<body>

  <h2>Contact Us</h2>

  <form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">

    <label for="email">Email:</label>
    <input type="email" id="email" name="email">

    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="5"></textarea>

    <button type="submit">Send</button>
  </form>

</body>
</html>
