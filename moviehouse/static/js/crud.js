
function onFormSubmit() {
    var formData = readFormData();
    insertNewRecord(formData);
}

function readFormData() {
    var formData = {};
    formData["cfname"] = document.getElementById("cfname").value;
    formData["clname"] = document.getElementById("clname").value;
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("castList").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.cfname;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.clname;
    // cell3 = newRow.insertCell(2);
    // cell3.innerHTML = `<a onClick="onEdit(this)">Edit</a>
    //                    <a onClick="onDelete(this)">Delete</a>`;
}