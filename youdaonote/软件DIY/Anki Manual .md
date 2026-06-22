通过问答的方式记忆

A good way to integrate active recall testing into your own studies is to use flashcards. With traditional paper flashcards, you write a question on one side of a card, and the answer on the other side. By not turning the card over until you’ve thought about the answer, you can learn things more effectively than passive observation allows.

 

 

复习抗遗忘

studies show we forget about 75% of material learnt within a 48 hour period. The solution is simple, however: review. By reviewing newly-learnt information, we can greatly reduce forgetting.

 

 

The program(SuperMemo) is often criticized for being buggy and difficult to navigate. It only runs on Windows computers.

 

A question and answer pair is called a card. This is based on a paper flashcard with a question on one side and the answer on the back. In Anki a card doesn’t actually look like a physical card, and when you show the answer the question remains visible by default.

card的解释（摘抄如上）和用法

https://apps.ankiweb.net/docs/manual.html#cards

 

 

deck =  group

 In this example, we have three pieces of related information: a French word, an English meaning, and a page number. If we put them together, they’d look like this:

French: Bonjour
English: Hello
Page: 12

In Anki, this related information is called a note, and each piece of information is called a field. So we can say that this type of note has three fields: French, English, and Page.



templates that says which fields should be displayed on the front or back of each card.



When Anki checks for duplicates, it only compares other notes of the same type（要有id，比如单词或正面卡）



简单的试试可以用别人做的卡片，如果是要有背景信息和理解的卡片的话需要自己做。



Below the fields is another area labelled “Tags”. Tags are labels that you can attach to your notes, to make organizing and finding notes easier. You can leave the tags blank if you wish, or add one or more of them. Tags are separated by a space. If the tags area says
vocab check_with_tutor
…then the note you add would have two tags



Anki checks the first field for uniqueness, so it will warn you if you enter two cards with a Front field of “apple” (for example). The uniqueness check is limited to the current note type, so if you’re studying multiple languages, two cards with the same Front would not be listed as duplicates as long as you had a different note type for each language.





























Addon

https://github.com/eshapard/experimentalCardEaseFactor

安装

Create a new folder named experimentalCardEaseFactor in your Anki 2.1 addons directory. Save __init__.py, experimentalCardEaseFactor.py and YesOrNo.py to this folder. If you don't want to use YesOrNo.py, don't include it, and remove it from __init__.py.

experimentalCardEaseFactor.py里showCardStats = False

disable Show next review time above answer buttons in Tools > Preferences...

安装后重启



https://ankiweb.net/shared/info/1481634779

安装后重启

![](attachments/Anki%20Manual%20_image_0.png)













