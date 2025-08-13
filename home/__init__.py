<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF_8">
<title>Menu Items</title>
<style>
  body { font_family: 'Arial, sans_serif; padding: 20px; }
  ul { list_style_type: none; padding:0; }
  li { padding: 10px; border_bottom: 1px solid}
</style>
</head>
<body>
<h1>Menu</h1>
<ul>
  <li>🍕 Pizza</li>
  <li>🍔 Burger</li>
  <li>🥗 salad</li>
  <li>🍝 Pasta</li>
  <li>🍰 Cake</li>
</ul>
</body>
</html>
 def menu_view(request):
    menu_items = ['pizza', 'burger', 'psata', 'salad', 'cake']
    return render(request, 'menu.html', {'menu_items': menu_items})

menu_items = Menu_items.pbjects.all()