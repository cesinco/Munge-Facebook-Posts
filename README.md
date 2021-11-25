# Munge Facebook Posts

## Description

Python program to munge text posted to Facebook to "encode" language that Facebook may potentially deem as abusive

## Details

OK - seriously. Who here has not received at least a 3-day ban to Facebook jail for calling someone a moron in a heated Facebook discussion? :)

Well, this little program will "encode" your posts using a little algorithm that we have all become familiar with that has made its rounds on Facebook itself in the form of a meme that mangles words, and yet the human brain is able to reconstruct them fairly easily so long as the first and last letter of each word remain in their original positions.

Knowing this, I developed this little program that takes a single line of text, and transforms it into a mangled version, preserving the first and last character in their correct positions, and swapping two characters (for shorter words) or 4 characters (for longer words) so that the words are no longer in the dictionary that Facebook likely uses to determine what is considered worthy of banning to Facebook jail.

This implies that each paragraph in your post needs to be munged/mangled separately, since a carriage return in your command-line input will cause the code to execute immediately. Alternatively, you could format your entire post as one long paragraph, and then split it into separate paragraphs as you post.

The program also specifically ignores non-alpha characters at the start and end of each "word" (a "word" is a series of characters being delimited by spaces). In cases where a "word" either starts or ends with non-alpha characters, these are temporarily excluded from mangling the words. Additionally, short words (those less than 4 characters) are also excluded from mangling. Words that are 4 characters or longer have some subset of their inner characters swapped.

## Requirements

Any recent version 3.x of Python, which includes regex and numpy libraries installed

## Examples

### The justification for this program

```
Enter text to be munged/mangled for posting to Facebook:

Hello World! This is an attempt to munge text when posting to Facebook, specifically to mangle words that ***might*** be "misconstrued" as abusive language.
Hlelo Wolrd! Tihs is an attepmt to mnuge txet wehn poitsng to Faceobok, spicifeaclly to mnagle wrods taht ***mhgit*** be "misocnstured" as avusibe lgnauage.
```

### A quote from one of my favorite authors and magicians, Penn Jillette

```
Enter text to be munged/mangled for posting to Facebook:

"The question I get asked by religious people all the time is, without God, what's to stop me from raping all I want? And my answer is: I do rape all I want. And the amount I want is zero. And I do murder all I want, and the amount I want is zero. The fact that these people think that if they didn't have this person watching over them that they would go on killing, raping rampages is the most self-damning thing I can imagine."
"The quesoitn I get aeksd by religuois plopee all the tmie is, wtihout God, waht's to sotp me form ranipg all I wnat? And my anewsr is: I do rpae all I wnat. And the amonut I wnat is zreo. And I do merdur all I wnat, and the amnuot I wnat is zreo. The fcat taht tehse peolpe tihnk taht if tehy ddin't hvae tihs pesron witchang oevr tehm taht tehy wluod go on killnig, raipng raepagms is the msot slef-dnmaing tihng I can imigane."
```

### A quote from another one of my favorite authors and thinkers, Sam Harris, but this time, just the mangled/munged version

```
"The prdsieent of the Unetid Stetas has cialmed, on mroe tahn one occisaon, to be in dialouge wtih God. If he siad taht he was tnlkiag to God turohgh his haridryer, tihs wuold pricepitate a natnoial emergnecy. I fial to see how the addition of a haerdryir mekas the cliam mroe ricidulous or ofiensfve."
```
