****************************************************************************************************************
****************************************************************************************************************
** Be careful! you're making a mistake? you don't understand me? that's not my problem...                     **
** Make a good backup before destroying everything...                                                         **
** You have been warned...                                                                                    **
****************************************************************************************************************
****************************************************************************************************************


There is no official way to populate user-added columns from a source Metadata extension.
To stay on the road, I decided to give the possibility to extend the field publisher with complementary information.

If we choose this option we will have publisher§collection€seriel-code in the publisher column.

To use this option, I created a column
"collection" (Lookup name: #collection, type: Text, column shown in the Tag browser)
"coll_srl" (Lookup name: #coll_srl, type: Long text, like comments, not shown in the Tag browser
           interpret this column as: Short text, like a title)

After the metadata research work, we can rectify by hand ...
OR
use edit metadata in bulk .. !!!.backup.!!!

preparation: use edit metadata in bulk

'Find and replace' tab
search field: publisher
Search for: .*§(.*)€(.*)
Replace with: \2
destination field: #Coll_srl
HERE WE SAVE and we give a name easy to find such as: "from publisher to #coll_str (separator § €)"

'Find and replace' tab
search field: publisher
Search for: .*§(.*)€(.*)
Replace with: \1
Destination field: #collection
HERE WE SAVE and we give a name easy to find such as: "from publisher to #collection (separator § €)"

'Find and replace' tab
search field: publisher
Search for: (.*)§(.*)
Replace with: \ 1
Destination field: Publisher
HERE WE SAVE and we give a name easy to find such as: "from publisher to publisher (we erase everything from §)"

We can now take action. Did you make a backup? no? do it...
in Calibre search for the § sign (paragraph sign) followed by enough letters to verify that is selected
what we want to rectify and nothing else
edit metadata in bulk
'Find and replace' tab
copy a line from a "Book" box to the "Your test" box
from Load search/replace: choose "from publisher to #coll_srl (separator § €)"
check that the expected result is indeed the one obtained under testing the result ... Apply
ditto with "from publisher to #collection (separator § €)"
and with "from publisher to publisher (we erase everything from §)"

we restore the backup if we screwed up (but we didn't screw up... yeahhh...)
