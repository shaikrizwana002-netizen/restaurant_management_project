<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF_8">
<title>Menu Items/title>
<style>
body{
    font_family: 'Arial, sans_serif;
    background_color: #f4f4f4;
    padding: 20px;
}
h1 {
    color: #333;
}

ul.menu_list {
    list_style_type: none;
    padding: 0;
}
ul.menu_item li {
    background_color: #fff;
    margin_bottom: 10px;
    padding: 10px;
    border_radius: 15px;
    box_shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
</head>
<body>

<h1>Menu_Items</h1>
<ul class="menu_list" id="menu_list"></ul>

<script>
// Hardcoded menu Itemsconst menuitems = [
    {name: "Home", link: "/" },
    {name: "About Us", limk: "/about" },
    {name: "Services", link: "/service" },
    {name: "Contact", link: "/contact" },
];
menuitems.foreach(item =>{
    const li = document.creareElement("li");
    li.textcontent = '₹{item.name} (₹{item.link})/;
    menulist.appendChild(li);
});
</script>
</body>
</html>

<script>
fetch('api/menu')
.then(response => response.json())
.then(data => {
    const menulist = document.getElementById("menu_list");
    data.forEach(item =>{
        const li = document.creareElement('li'):
        li.textContent = '₹{item.name} (₹{item.link})';
        menulist.appendChild(li);
    });
})
.catch(error => console.error('Error fetching mennnnnu items:'));
</script>