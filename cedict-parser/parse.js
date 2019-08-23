// parse cedict into dictionary language resource
var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('./cedict_ts.u8')
});



var terms = {}
var pinyin = require('pinyin')
lineReader.on('line', function (line) {
  // console.log(line);
  let parts = line.split(" /");
  var text = parts[0].split(" ")[1]
  var meaning = parts.slice(1).join("");
  var term = {
    text: text,
    meaning: "/"+pinyin(text, 
      {heteronym:true,segment:true})
      .join(" ")+"/"+"\n"+ "* "+meaning.replace(/(\/)(.)/g, "\n* $2").replace(/\//g,"")
  }

  if(terms[text]) {
terms[text].meaning += "\n"+term.meaning;
  }
  else 
  //console.log(JSON.stringify(term))
  terms[text] = term;
});


lineReader.on('close', () => {
const fs = require('fs');
terms = Object.keys(terms).map(k => 
  terms[k]
)

fs.writeFile("./zh-en.json", JSON.stringify(terms, null, 2), function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
}); 
});