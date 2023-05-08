window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    const datatablesSimple2 = document.getElementById('datatablesSimple2');
    const datatablesSimple3 = document.getElementById('datatablesSimple3');
    const datatablesSimple4 = document.getElementById('datatablesSimple4');
    const datatablesSimple5 = document.getElementById('datatablesSimple5');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
    if (datatablesSimple2) {
        new simpleDatatables.DataTable(datatablesSimple2);
    }
    if (datatablesSimple3) {
        new simpleDatatables.DataTable(datatablesSimple3);
    }
    if (datatablesSimple4) {
        new simpleDatatables.DataTable(datatablesSimple4);
    }
    if (datatablesSimple5) {
        new simpleDatatables.DataTable(datatablesSimple5);
    }
});
