document.addEventListener('DOMContentLoaded', function() {
  const colorBox = document.getElementById('colorBox');
  const changeColorBtn = document.getElementById('changeColorBtn');
  
  const colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6'];
  let currentColorIndex = 0;
  
  changeColorBtn.addEventListener('click', function() {
    currentColorIndex = (currentColorIndex + 1) % colors.length;
    colorBox.style.backgroundColor = colors[currentColorIndex];
  });
});
