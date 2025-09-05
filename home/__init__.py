<nav class="breadcrumb">
  <a href="/home">Home</a>
  <span></span>
  <a href="Projects">Projects</a>
  <a href="/prijects/tasks">Tasks</a>
  <span></span>
  <span class="current">View Tasks</span>
  </nav>

.breadcrumb {
    font-family: Arial,sans-serif;
    font-size:14px;
    margin: 20px 0;
    padding: 8px 16px;
    border-radius: 4px;
    background-color: #5f5f5;
    gap: 8px;
    display: flex;
    flex-wrap: wrap;
}  

.breadcrumb {
    color: #007bff;
}
.breadcrumb a:hover { 
    text-decoration: underline;
}

.breadcrumb .current {
    color: #555;
    font-weight: bold;
}