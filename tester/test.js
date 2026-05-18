document.addEventListener("DOMContentLoaded", () => {
  const addBtn = document.querySelector('.add_request');
  const tableBody = document.querySelector('.requests-table tbody');

  addBtn.addEventListener('click', () => {
    const newRow = document.createElement('tr');
    const uniqueId = Date.now();

    newRow.innerHTML = `
      <td><input type="text" class="edit-product" placeholder="Product"></td>
      <td>
        <input type="number" class="edit-quantity" style="width: 60px;">
        <select class="unit-select">
          <option value="L">L</option>
          <option value="kg">kg</option>
          <option value="ton">ton</option>
          <option value="pcs">pcs</option>
        </select>
      </td>
      <td><input type="text" class="edit-country" placeholder="Country"></td>
      <td><input type="date" class="edit-request-date"></td>
      <td><input type="date" class="edit-deadline"></td>
      <td>
        <input type="radio" id="status_open_${uniqueId}" name="status_${uniqueId}" checked>
        <label for="status_open_${uniqueId}">Open</label>
        <input type="radio" id="status_close_${uniqueId}" name="status_${uniqueId}">
        <label for="status_close_${uniqueId}">Close</label>
      </td>
      <td><button class="action-btn view-details-btn">View</button></td>
      <td><button class="action-btn delete-btn">Delete</button></td>
      <td><button class="action-btn edit-btn">Save</button></td>
    `;

    tableBody.appendChild(newRow);

    // кнопка Delete
    newRow.querySelector('.delete-btn').addEventListener('click', () => {
      newRow.remove();
    });

    // кнопка Save/Edit
    newRow.querySelector('.edit-btn').addEventListener('click', (e) => {
      const btn = e.target;
      if (btn.textContent === "Save") {
        btn.textContent = "Edit";
        newRow.querySelectorAll('input, select').forEach(el => el.disabled = true);
      } else {
        btn.textContent = "Save";
        newRow.querySelectorAll('input, select').forEach(el => el.disabled = false);
      }
    });
  });
});
