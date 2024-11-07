import os
from baseball_scorecard.baseball_scorecard import Scorecard

# HOU @ BOS, 2013-04-25
# https://www.baseball-reference.com/boxes/BOS/BOS201304250.shtml
# https://www.mlb.com/gameday/astros-vs-red-sox/2013/04/25/347067/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-25 18:36-21:35",
        "at": "Fenway Park, Boston, MA",
        "att": "30,093",
        "temp": "63F, Partly Cloudy",
        "wind": "10mph, Out To RF",
        "away": {
            "team": "Houston Astros",
            "starter": 59,
            "roster": {
                # Lineup
                19: "Robbie Grossman",
                27: "Jose Altuve",
                15: "Jason Castro",
                12: "Carlos Pena",
                23: "Chris Carter",
                21: "Fernando Martinez",
                30: "Matt Dominguez",
                28: "Rick Ankiel",
                9: "Marwin Gonzalez",
                # Starting pitcher
                59: "Philip Humber",
                # Bench
                13: "Ronny Cedeno",
                4: "Brandon Laird",
                2: "Brandon Barnes",
                22: "Carlos Corporán",
                # Bullpen
                45: "Erik Bedard",
                62: "Hector Ambriz",
                53: "Wesley Wright",
                20: "Bud Norris",
                64: "Lucas Harrell",
                41: "Jose Veras",
                54: "Travis Blackley",
                56: "Paul Clemens",
                43: "Brad Peacock",
                68: "José Cisnero",
                55: "Rhiner Cruz",
            },
            "lefties": [45, 53, 54],
            "lineup": [
                [19, "8"],
                [27, "4"],
                [15, "2"],
                [12, "3"],
                [23, "0"],
                [21, "7"],
                [30, "5"],
                [28, "9"],
                [9, "6"],
            ],
            "bench": [
                [13, "SS"],
                [4, "3B"],
                [2, "CF"],
                [22, "C"],
            ],
            "bullpen": [45, 62, 53, 20, 64, 41, 54, 56, 43, 68, 55],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                18: "Shane Victorino",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                51: "Daniel Bard",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [18, "CF"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 30, 31, 59, 36, 51, 19, 22, 46],
        },
        "umpires": {
            "HP": "Tim McClelland",
            "1B": "Jerry Meals",
            "2B": "Marvin Hudson",
            "3B": "Jordan Baker",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. HOU #19 Robbie Grossman (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G3")

# 2. HOU #27 Jose Altuve (X - X - X)
t1.new_ab()
t1.pitch_list("b b c c b c")
t1.out("!K")

# 3. HOU #15 Jason Castro (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c b")
t1.reach("BB")

# 4. HOU #12 Carlos Pena (X - X - 15)
t1.new_ab()
t1.out("B1-3")


# Bot 1st
# Pitching: HOU #59 Philip Humber
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b c b b f")
b1.out("G4-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b b")
b1.reach("BB")
b1.advance(2, "15 PB")
b1.advance(4, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.pb()
b1.hit(1, rbis=1)
b1.advance(2, "34 SB")
b1.advance(4, "34 E9")

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.hit(1, rbis=1)
b1.error(9)
b1.advance(2, "E9")
b1.advance(4, "37 2B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b b b f t")
b1.out("KT")

# 6. BOS #37 Mike Carp (X - 34 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c f")
b1.hit(2, rbis=1)
b1.advance(4, "39 1B")

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s")
b1.hit(1, rbis=1)

# 8. BOS #16 Will Middlebrooks (X - X - 39)
b1.new_ab()
b1.pitch_list("f b f")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 5. HOU #23 Chris Carter (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.hit(2)
t2.advance(3, "21 1B")
t2.advance(4, "30 DP4-3")

# 6. HOU #21 Fernando Martinez (X - 23 - X)
t2.new_ab(is_risp=True)
t2.hit(1)
t2.thrown_out(2, "30 DP4-3", 1, 11)

# 7. HOU #30 Matt Dominguez (23 - X - 21)
t2.new_ab(is_risp=True)
t2.pitch_list("b 1 1 b b c 1 f f f")
t2.out("DP4-3")

# 8. HOU #28 Rick Ankiel (X - X - X)
t2.new_ab()
t2.pitch_list("c f f f b b b f s")
t2.out("K")


# Bot 2nd
# Pitching: HOU #59 Philip Humber
b2 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b2.new_ab()
b2.hit(2)

# 2. BOS #29 Daniel Nava (X - 2 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b b c b")
b2.reach("BB")
b2.thrown_out(2, "15 DP5-4-3", 2, 59)

# 3. BOS #15 Dustin Pedroia (X - 2 - 29)
b2.new_ab(is_risp=True)
b2.out("DP5-4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 9. HOU #9  Marwin Gonzalez (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b")
t3.hit(2)
t3.advance(3, "27 SB")
t3.advance(4, "15 1B")

# 1. HOU #19 Robbie Grossman (X - 9 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b f s")
t3.out("K")

# 2. HOU #27 Jose Altuve (X - 9 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b b b c f c")
t3.out("!K")

# 3. HOU #15 Jason Castro (9 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b")
t3.hit(1, rbis=1)

# 4. HOU #12 Carlos Pena (X - X - 15)
t3.new_ab()
t3.pitch_list("f 1 b s d b c")
t3.out("!K")


# Bot 3rd
# Pitching: HOU #59 Philip Humber
b3 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(4)

# 5. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("s s b s")
b3.out("K")

# 6. BOS #37 Mike Carp (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G6-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 5. HOU #23 Chris Carter (X - X - X)
t4.new_ab()
t4.pitch_list("c s b b s")
t4.out("K")

# 6. HOU #21 Fernando Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.thrown_out(2, "30 DP5-4-3", 2, 11)

# 7. HOU #30 Matt Dominguez (X - X - 21)
t4.new_ab()
t4.pitch_list("1")
t4.out("DP5-4-3")


# Bot 4th
# Pitching: HOU #59 Philip Humber
b4 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("b b s f s")
b4.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b c f b")
b4.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b4.new_ab()
b4.pitch_list("1 b c")
b4.out("F7")

# 2. BOS #29 Daniel Nava (X - X - 7)
b4.new_ab()
b4.pitch_list("c c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 8. HOU #28 Rick Ankiel (X - X - X)
t5.new_ab()
t5.pitch_list("f b b b b")
t5.reach("BB")
t5.thrown_out(2, "27 FC4-6", 3, 11)

# 9. HOU #9  Marwin Gonzalez (X - X - 28)
t5.new_ab()
t5.pitch_list("1 1 c 1 f s")
t5.out("K")

# 1. HOU #19 Robbie Grossman (X - X - 28)
t5.new_ab()
t5.out("F7")

# 2. HOU #27 Jose Altuve (X - X - 28)
t5.new_ab()
t5.reach("FC4-6")


# Bot 5th
# Pitching: HOU #59 Philip Humber
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.advance(3, "37 1B")
b5.advance(4, "39 1B")

# 5. BOS #12 Mike Napoli (X - X - 34)
b5.new_ab()
b5.pitch_list("s b c b c")
b5.out("!K")

# 6. BOS #37 Mike Carp (X - X - 34)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "39 1B")
b5.advance(4, "16 2B")

# 7. BOS #39 Jarrod Saltalamacchia (34 - X - 37)
b5.new_ab(is_risp=True)
b5.pitch_list("b 1 s")
b5.hit(1, rbis=1)
b5.advance(3, "16 2B")

# 8. BOS #16 Will Middlebrooks (X - 37 - 39)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.hit(2, rbis=1)

# Pitching change (HOU): #54 Travis Blackley replaces #59 Philip Humber
b5.pitching_substitution(54)

# 9. BOS #7  Stephen Drew (39 - 16 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c s d")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 3. HOU #15 Jason Castro (X - X - X)
t6.new_ab()
t6.pitch_list("c f b c")
t6.out("!K")

# 4. HOU #12 Carlos Pena (X - X - X)
t6.new_ab()
t6.out("G4-3")

# 5. HOU #23 Chris Carter (X - X - X)
t6.new_ab()
t6.pitch_list("c c b b")
t6.out("G4-3")


# Bot 6th
# Pitching: HOU #54 Travis Blackley
b6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("c b c s")
b6.out("K")

# 2. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b f f b s")
b6.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("s s b b f b f d")
b6.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b6.new_ab()
b6.pitch_list("1 1 f s 1")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #11 Clay Buchholz
t7 = game.new_inning()

# 6. HOU #21 Fernando Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b c b s")
t7.out("G6-3")

# 7. HOU #30 Matt Dominguez (X - X - X)
t7.new_ab()
t7.pitch_list("c s b c")
t7.out("!K")

# 8. HOU #28 Rick Ankiel (X - X - X)
t7.new_ab()
t7.pitch_list("b b c f c")
t7.out("!K")


# Bot 7th
# Pitching: HOU #68 José Cisnero
b7 = game.new_inning()

# Pitching change (HOU): #68 José Cisnero replaces #54 Travis Blackley
b7.pitching_substitution(68)

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("c s b")
b7.hit(2)

# 6. BOS #37 Mike Carp (X - 12 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f b")
b7.out("(F)P5")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s")
b7.out("(F)P5")

# 8. BOS #16 Will Middlebrooks (X - 12 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c f b f f f b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #11 Clay Buchholz
t8 = game.new_inning()

# Defensive change (BOS): #5 Jonny Gomes replaces #37 Mike Carp (LF), playing LF, batting 6th
t8.defensive_substitution(6, 5, "7")

# 9. HOU #9  Marwin Gonzalez (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")

# 1. HOU #19 Robbie Grossman (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")

# 2. HOU #27 Jose Altuve (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.hit(1)

# Pitching change (BOS): #30 Andrew Miller replaces #11 Clay Buchholz
t8.pitching_substitution(30)

# 3. HOU #15 Jason Castro (X - X - 27)
t8.new_ab()
t8.pitch_list("f b d")
t8.out("F7")


# Bot 8th
# Pitching: HOU #68 José Cisnero
b8 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G5-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("L8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #51 Daniel Bard
t9 = game.new_inning()

# Pitching change (BOS): #51 Daniel Bard replaces #30 Andrew Miller
t9.pitching_substitution(51)

# 4. HOU #12 Carlos Pena (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("F7")

# 5. HOU #23 Chris Carter (X - X - X)
t9.new_ab()
t9.pitch_list("b c b s b f s")
t9.out("K")

# 6. HOU #21 Fernando Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("b b c")
t9.hit(1)

# 7. HOU #30 Matt Dominguez (X - X - 21)
t9.new_ab()
t9.pitch_list("b b b c")
t9.out("G1-3")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11)

# Loser team: HOU
# LP: HOU #59 Philip Humber
game.losing_pitcher(59, is_away_team=True)

# print(game)
game.generate_scorecard()
