let attendanceData = {};

async function fetchAttendance() {
    try {
        const response = await fetch('/data');
        const data = await response.json();
        attendanceData = data;
        updateTable();
        updateChart();
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

function updateTable() {
    const tableBody = document.getElementById('attendance-table');
    const filter = document.getElementById('filter').value;
    const searchText = document.getElementById('search-input').value.toLowerCase();

    tableBody.innerHTML = '';

    for (let id in attendanceData) {
        const student = attendanceData[id];

        if (filter === 'verified' && !student.verified) continue;
        if (filter === 'unverified' && student.verified) continue;

        if (
            !student.name.toLowerCase().includes(searchText) &&
            !student.barcode.toLowerCase().includes(searchText)
        ) continue;

        const row = `
            <tr>
                <td><img src="${student.image_url}" width="40" height="40" style="border-radius:50%;"></td>
                <td>${student.name}</td>
                <td>${student.barcode}</td>
                <td>${student.entry_time}</td>
                <td>${student.verified ? '✅' : '❌'}</td>
            </tr>
        `;
        tableBody.innerHTML += row;
    }
}

function updateChart() {
    const verified = Object.values(attendanceData).filter(s => s.verified).length;
    const unverified = Object.values(attendanceData).filter(s => !s.verified).length;

    attendanceChart.data.datasets[0].data = [verified, unverified];
    attendanceChart.update();
}

function exportToExcel(){
    const rows =[['Name', 'Barcode', 'Entry Time', 'Exit Time', 'Verified']];
    for (let id in attendanceData){
        const s= attendanceData[id];
        rows.push([s.name, s.barcode, s.entry_time, s.exit_time, s.verified ? 'Yes' : 'No']);
    }

    let csvContent= "data:text/csv; charset=utf-8," + rows.map(e => e,join(",")).join("\n");
    const encodedUri = encodeURI(csvContent);


    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "attendance_data.csv");

    document.body.appendChild(link);


    link.click();

}


const ctx=document.getElementById('attendanceChart').getContext('2d');
const attendanceChart = new CharacterData(ctx,{
    type: 'doughnut',
    data: {
        labels: ['Verified ✅', 'Unverified ❌'],
        datasets : [{
            data: [0, 0],
            backgroundColor: ['#28a745', '#dc3545'],
        }]

    },
    options: {
        responsive: true,
        plugins: {
            legend: { position: 'bottom'},
            title: {
                display: true,
                text: 'Attendace Verification  Status'
            }
        }
    }
});




document.getElementById('filter').addEventListener('change', updateTable);
document.getElementById('search-input').addEventListener('input', updateTable);

setInterval(fetchAttendance, 5000);
fetchAttendance();
