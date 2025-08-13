<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF_8">
<title>Contact Us</title>
<style>
  body { font_family: 'Arial, sans_serif; padding: 20px; }
 .contact_box {max_width: 500px: margin:auto; border: 1px solid #ccc; padding: 15px; border_radius: 8px; }
 hi { text_align: center; }
 p {margin: 10px 0;}
 </style>
</head>
<body>
  <div class="contact_box>
      <h1>Contact Us</h1>
      <p><strong>Company:</strong> {{ contact_info.company_name }}<p/>
      <p><strong>Email:</strong> {{contact_info.email }}</p>
      <p><strong>Phone:</strong> {{ company_phone }}</p>
      <p><strong>Address:</strong> {{ company_address }}</p>
  </div>
</body>
</html>