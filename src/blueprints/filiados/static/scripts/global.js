function confirmarDownload() {    
    if (confirm("Deseja fazer download das planilhas do TSE? operação demorada") == true) {
        document.getElementById("botaoDownload").disabled;
        document.getElementById('modalcarga').style.display = "block";
        return true;
    } else {
        return false;
    }
}

