// A javascript-enhanced crossword puzzle [c] Jesse Weisbeck, MIT/GPL 
(function($) {
	$(function() {
		// provide crossword entries in an array of objects like the following example
		// Position refers to the numerical order of an entry. Each //position can have 
		// two entries: an across entry and a down entry
		var puzzleData = [
			 	{
					clue: "Oh don’t you wish this place was closer to home, for both of us.",
					answer: "ahmedabad",
					position: 3,
					orientation: "down",
					startx: 1,
					starty: 1
				},
			 	{
					clue: "You should probably not step on this in a war zone. But more importantly while talking to Sanskriti.",
					answer: "landmine",
					position: 2,
					orientation: "across",
					startx: 3,
					starty: 3
				},
				{
					clue: "Sadly we’ll have to do this on the same day in whenever you’re in Delhi.",
					answer: "checkout",
					position: 1,
					orientation: "across",
					startx: 3,
					starty: 1
				},
				{
					clue: "Complete lack of safety regulations. Also a famous explorer.",
					answer: "columbus",
					position: 1,
					orientation: "down",
					startx: 3,
					starty: 1
				},
				{
					clue: "Name has 2 parts. Second part is Malabar word for peacock’s tail. Naming of first part should make sense now. (And also should its logo). Also, a cool place to go when you’re not in the mood for Delhi.",
					answer: "bluetokai",
					position: 4,
					orientation: "across",	
					startx: 1,
					starty: 7
				},
				{
					clue: "Oriental food is a 4-letter word for Sansky, but this dish, with one letter less, is just the opposite.",
					answer: "bao",
					position: 5,
					orientation: "down",
					startx: 6,
					starty: 5
				},
				{
					clue: "Married women break this when husband dies. However, when Sanskriti breaks this, she feels 50% overwhelmed, 30% saddened, and 20% hopeful.",
					answer: "bangle",
					position: 7,
					orientation: "down",
					startx: 8,
					starty: 6
				},
				{
					clue: "Humans do this to show affection. I ain’t particularly adept at it, when you meet me for the first time (or maybe that’s because you’re too short :P)",
					answer: "hugging",
					position: 6,
					orientation: "across",
					startx: 6,
					starty: 9
				},
				{
					clue: "What does my name mean? (Hint : “Accomplishment from ___”)",
					answer: "willpower",
					position: 8,
					orientation: "across",
					startx: 1,
					starty: 11
				},
				{
					clue: "A very special symbol, I hope (:P) I never lose (again) (*monkey emoji*)",
					answer: "bell",
					position: 9,
					orientation: "down",
					startx: 4,
					starty: 9
				},
				{
					clue: "“Theobroma should start making desserts ___ sugar”.",
					answer: "without",
					position: 11,
					orientation: "down",
					startx: 18,
					starty: 1
				},
				{
					clue: "Out of all your boys, I’m the only one that’s ___ than you. (Arjun doesn’t count :P)",
					answer: "younger",
					position: 10,
					orientation: "across",
					startx: 14,
					starty: 12
				},
				{
					clue: "“The sun rises in the East, and therefore the East is called ___”.  Maybe next time we watch a movie like this, the 80-20 rule would apply :P",
					answer: "orient",
					position: 12,
					orientation: "across",
					startx: 13,
					starty: 3
				},
				{
					clue: "Combine ___ sorbet, and vanilla gelato, and you get an egg shaped dessert (maybe that’s why it’s called Easter? :P). At a place cool enough to attract fellow GNLU seniors.",
					answer: "mango",
					position: 13,
					orientation: "down",
					startx: 12,
					starty: 6
				},
				{
					clue: "Old Turkish word for “covering garment”. Also a cool hippie gift.",
					answer: "kaftan",
					position: 14,
					orientation: "across",
					startx: 11,
					starty: 7
				},
				{
					clue: "When people asked Albert Einstein to explain this, he said “Put your hand on a hot stove for a minute, and it seems like an hour. Sit with a pretty girl for an hour, and it seems like a minute”. Also helps explain the lightning-fast replies of Ms. Sanghi.",
					answer: "relativity",
					position: 15,
					orientation: "down",
					startx: 14,
					starty: 3
				}
			] 
	
		$('#puzzle-wrapper').crossword(puzzleData);
		
	})
	
})(jQuery)
