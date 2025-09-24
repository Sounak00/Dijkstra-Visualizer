async function parseGraph() {
    const text = document.getElementById('graphText').value;
    const resp = await fetch('/api/parse', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({text})
    });
    const data = await resp.json();
    showMatrix(data.nodes, data.matrix);
}


function showMatrix(nodes, matrix){
    const wrap = document.getElementById('matrixWrapper');
    if(nodes.length===0){ 
        wrap.innerHTML = '<p>No nodes parsed.</p>'; 
        return; 
    }
    let html = '<table><thead><tr><th></th>';
    nodes.forEach(n => html += `<th>${n}</th>`);
    html += '</tr></thead><tbody>';
    for(let i=0;i<nodes.length;i++){
        html += `<tr><th>${nodes[i]}</th>`;
        for(let j=0;j<nodes.length;j++){
            const val = matrix[i][j];
            html += `<td>${val===-1?'-':val}</td>`;
        }
        html += '</tr>';
    }
    html += '</tbody></table>';
    wrap.innerHTML = html;
}


async function computeShortest(){
const text = document.getElementById('graphText').value;
const source = document.getElementById('sourceInput').value.trim();
const destination = document.getElementById('destInput').value.trim();
const resDiv = document.getElementById('result');
resDiv.innerHTML = 'Computing...';
try{
const resp = await fetch('/api/shortest',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text,source,destination})});
const data = await resp.json();
if(data.error){ resDiv.innerHTML = `<b>Error:</b> ${data.error}`; return; }
if(!data.path){ resDiv.innerHTML = `<b>No path found</b>`; return; }
resDiv.innerHTML = `<b>Path:</b> ${data.path.join(' -> ')}<br/><b>Distance:</b> ${data.distance}`;
}catch(err){ resDiv.innerHTML = 'Error: '+err.message }
}


window.addEventListener('DOMContentLoaded', ()=>{
document.getElementById('parseBtn').addEventListener('click', parseGraph);
document.getElementById('shortestBtn').addEventListener('click', computeShortest);
// show matrix initially
parseGraph();
});