from django.shortcuts import render
from django.views import View # <- View class to handle request
from django.http import HttpResponse 
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Actor:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

actors = [
    Actor("Kevin Costner", "https://ntvb.tmsimg.com/assets/assets/36838_v9_bc.jpg?w=270&h=360", 
          "Kevin Costner is an American actor and filmmaker. He has received various accolades, including two Academy Awards, three Golden Globe Awards, a Primetime Emmy Award, and two Screen Actors Guild Awards."),

    Actor("Jennifer Grey", "https://www.thesun.co.uk/wp-content/uploads/2017/08/nintchdbpict000005058542.jpg",
          "Jennifer Grey is an American actress, known for her roles in the 1980s films Ferris Bueller's Day Off and Dirty Dancing."),

    Actor("Irene Cara", "https://www.thesun.co.uk/wp-content/uploads/2022/11/street-tale-hollywood-premiere-laemmle-778439188.jpg", 
          "Irene Cara is an American singer, songwriter, dancer, and actress, known for her roles in Fame."),

    Actor("Sigourney Weaver", "https://m.media-amazon.com/images/M/MV5BMTk1MTcyNTE3OV5BMl5BanBnXkFtZTcwMTA0MTMyMw@@._V1_.jpg", 
          "Sigourney Weaver is an American actress. Dubbed \"The Sci-Fi Queen\", Weaver is considered to be a pioneer of action heroines in science fiction films."),

    Actor("Harrison Ford", "https://upload.wikimedia.org/wikipedia/commons/3/34/Harrison_Ford_by_Gage_Skidmore_3.jpg",
          "Harrison Ford is an American actor, pilot, and environmental activist. He gained worldwide fame for his starring role as Han Solo in the Star Wars franchise and as the title character of the Indiana Jones film series."),

    Actor("Bill Murray", "https://static1.purepeople.com/articles/7/76/96/7/@/588186-bill-murray-incarnera-bientot-franklin-580x0-2.jpg",
          "Bill Murray is an American actor, comedian, and writer. Known for his deadpan delivery, he first rose to fame on Saturday Night Live, a series of performances that earned him his first Emmy Award."),

    Actor("Eddie Murphy", "https://parade.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTkwNTgxMDM0Nzk5ODAyMjM2/eddie-murphy-ftr.jpg",
          "Eddie Murphy is an American actor, comedian, writer, producer, and singer. He was a regular cast member on Saturday Night Live from 1980 to 1984. He has worked as a stand-up comedian and was ranked No. 10 on Comedy Central's list of the 100 Greatest Stand-ups of All Time."),

    Actor("Wil Wheaton", "https://yt3.googleusercontent.com/ytc/AGIKgqPDxvFqPmpGyN8PdLwK2zde7OKxwoeQ9D0JIKnToEI=s900-c-k-c0x00ffffff-no-rj",
          "Wil Wheaton is an American actor, blogger, and writer. He portrayed Wesley Crusher on the television series Star Trek: The Next Generation, Gordie Lachance in the film Stand by Me, Joey Trotta in Toy Soldiers, and Bennett Hoenicker in Flubber."),

    Actor("Tom Hanks", "https://flxt.tmsimg.com/assets/62982_v9_bb.jpg",
          "Tom Hanks is an American actor and filmmaker. Known for both his comedic and dramatic roles, he is one of the most popular and recognizable film stars worldwide, and is regarded as an American cultural icon."),

    Actor("Sandra Bullock", "https://www.emdria.org/wp-content/uploads/2021/12/Sandra-Bullock-Shutterstock-scaled.jpg",
          "Sandra Bullock is an American actress and producer. The recipient of various accolades, including an Academy Award and a Golden Globe Award, she was the world's highest-paid actress in both 2010 and 2014."),

    Actor("Shia LaBeouf", "https://pyxis.nymag.com/v1/imgs/532/b98/d38941d9d53cc5fbb60f760a6b90cc8287-shia-labeouf.rsquare.w330.jpg",
          "Shia LaBeouf is an American actor, performance artist, and filmmaker. He played Louis Stevens in the Disney Channel series Even Stevens, a role for which he received a Young Artist Award nomination in 2001 and won a Daytime Emmy Award in 2003."),

    Actor("Bruce Willis", "https://m.media-amazon.com/images/M/MV5BMjA0MjMzMTE5OF5BMl5BanBnXkFtZTcwMzQ2ODE3Mw@@._V1_FMjpg_UX1000_.jpg",
          "Bruce Willis is an American actor and film producer. His career began on the Off-Broadway stage in the 1970s."),

    Actor("Rami Malek", "https://flxt.tmsimg.com/assets/330277_v9_bb.jpg",
          "Rami Malek is an American actor. He is known for his lead role as Elliot Alderson in the television series Mr. Robot, for which he received the Primetime Emmy Award for Outstanding Lead Actor in a Drama Series."),

    Actor("Daniel Brühl", "https://www.themoviedb.org/t/p/w500/3YlmTfiy5qZXkrdKGjaM1uMjGKP.jpg",
          "Daniel Brühl is a Spanish-German actor. He began his work at a young age in a German soap opera called Forbidden Love in 1995."),

    Actor("Marilyn Monroe", "https://hips.hearstapps.com/hmg-prod/images/news-photo-515346396-1562946515.jpg",
          "Marilyn Monroe was an American actress, model, and singer. Famous for playing comedic \"blonde bombshell\" characters, she became one of the most popular sex symbols of the 1950s and early 1960s and was emblematic of the era's changing attitudes towards sexuality."),
]
