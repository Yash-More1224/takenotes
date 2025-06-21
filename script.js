async function save_notes(){
    // runs when save button is clicked
    const title = document.getElementById("note_title").value
    const note = document.getElementById("ipbox").value

    const res = await fetch('/save-notes', {
        method: 'post', 
        headers: {'Contet-Type':"application/json"}, 
        body: JSON.stringify({"title": title, "content": note}, null, 2)        
    });

    const response = await res.json()
    console.log(response.json())
}