
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".products-grid").forEach(grid => {
    const categoryElement = grid.closest(".event-category")?.querySelector(".category-header");
    if (!categoryElement) return;

    const categoryName = categoryElement.dataset.category
      ? categoryElement.dataset.category.replace(/-/g, " ").replace(/\w/g, l => l.toUpperCase())
      : null;

    const subcategory = grid.parentElement.id
      .split("-")
      .pop()
      .replace(/\w/g, l => l.toUpperCase());

    if (imageManifest[categoryName] && imageManifest[categoryName][subcategory]) {
      const images = imageManifest[categoryName][subcategory];
      grid.innerHTML = images
        .map(img => `
          <div class="product-card">
            <div class="product-image-container">
              <img src="\${img}" class="product-image" alt="\${categoryName} \${subcategory}">
            </div>
            <div class="product-info">
              <div class="product-pricing">
                <span class="old-price">₹\${grid.dataset.priceOld}</span>
                <span class="new-price">₹\${grid.dataset.priceNew}</span>
                <span class="discount-badge">SALE</span>
              </div>
              <button class="add-to-cart-btn">Add to Cart</button>
            </div>
          </div>
        `)
        .join("");
    }
  });
});
