Reference : [reference](https://dictionaryapi.com/products/json#term-headword)  
API: [api](https://www.dictionaryapi.com/api/v3/references/sd2/json/word?key=your-api-key)  
  
check if the word exists as entry in the dictionary, if not there will be the simple list of the suggestions  
	display all the suggestions, and ask user to choose any one of them, and again make the request  

check for homographs : words with the same spelling but different meanings eg. wind  
	in such case there is a list of dictionaries for each meaning, the most outer list  
	Normal cases that list has only one element / dictionary  
  	
>  Hence, iterate through the outer list to show the meaning  
  
  
**The sense** is a key organizational unit of the entry, and gathers together all content relevant to a particular meaning of a headword.  
sense can contain : prs(pronounciation) , vrs(variants), (All type of lables eg lbs) eg("often capitalized")

There can be verb dividers(vd) if verb can be both transitive & intransitive.  

**def**: contains list of dictionaries with keys as sense sequences(sseq) and verb dividers(vd) (if any), **occurs at top level member of dict**  
	if no vd then single dictionary in the list without vd, else multiple (2) dicts in the list with different vd's and corresponding sseqs  

"def":[  
  {  
    "vd":"transitive verb",  
    "sseq":[  
      [  
        [  
          "sense",  
          {  
            "dt":[["text","{bc}to place in or bring into a boat"]]  
          }  
        ]  
      ]  
    ]  
  },{  
    "vd":"intransitive verb",  
    "sseq":[  
      [  
        [   
          "sense",  
          {  
            "dt":[["text","{bc}to go by boat"]]  
          }  
        ]  
      ]  
    ]  
  }  
]  

> Hence, iterate through the list of dicts in def to display all meanings  

**sseq** : is a list of list of senses(which is also a list) and (subsenses if any), **occurs inside def**  

> Hence, iterate through the list (_which has list of lists(senses)_) to display all the meanings  
> While iterating check that 1st member of list inside a list is 'sense' or not  

if there are multiple senses, then there is sense number (sn) in the **dict in the list of particular _sense_**  
sense number identifies the sense number or a subsense number  

 __the list is like this -> ["sense", {dict}]__  

**defining text (dt)**: This is another (mandatory) key in the above _dict_ which contains the meaning  
Its value is a list having multiple(optional, can be single as well) lists having this format -> **["text", string]** where string contains the definition content (required)  

optinal elements instead of text: **bnw, ca, ri, snote, uns, or vis**  
	bnw : biographical name wrap (parents name + surname etc)  
	ca: called also  
	ri: run-in entry word  
	snote: provides explanatory or historical information that supplements the definition text  
	uns: Provide usage information on a headword, defined run-on phrase, or undefined entry word.  
	vis: verbal illustration (how the word is used in the context)

We _might_ be interested only in vis	  

//check sdsense and sen as well, if they occur then its complicated !  

**Short Defination**:  
A short definition provides a highly abridged version of the main definition section, consisting of just the definition  
text for the first three senses. It is not meant to be displayed along with the full entry, but instead as an  
alternative, shortened preview of the entry content. A short definition is contained in a shortdef.  

**occurs at top level member of dict**  
It is a simple list, print out the elements in it

key: 'shortdef'

#### We will be printing senses->dt->text strings and shortdefs

