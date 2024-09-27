import os
from baseball_scorecard.baseball_scorecard import Scorecard

# HOU @ BOS, 2013-04-28
# https://www.baseball-reference.com/boxes/BOS/BOS201304280.shtml
# https://www.mlb.com/gameday/astros-vs-red-sox/2013/04/28/347111/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-28 13:34-16:30",
        "at": "Fenway Park, Boston, MA",
        "att": "36,527",
        "temp": "59F, Partly Cloudy",
        "wind": "13mph, In From RF",
        "away": {
            "team": "Houston Astros",
            "starter": 20,
            "roster": {
                # Lineup
                19: "Robbie Grossman",
                27: "Jose Altuve",
                15: "Jason Castro",
                12: "Carlos Pena",
                13: "Ronny Cedeno",
                21: "Fernando Martinez",
                30: "Matt Dominguez",
                28: "Rick Ankiel",
                9: "Marwin Gonzalez",
                # Starting pitcher
                20: "Bud Norris",
                # Bench
                23: "Chris Carter",
                4: "Brandon Laird",
                2: "Brandon Barnes",
                22: "Carlos Corporán",
                # Bullpen
                45: "Erik Bedard",
                62: "Hector Ambriz",
                53: "Wesley Wright",
                64: "Lucas Harrell",
                41: "Jose Veras",
                59: "Philip Humber",
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
                [13, "0"],
                [21, "7"],
                [30, "5"],
                [28, "9"],
                [9, "6"],
            ],
            "bench": [
                [23, "1B"],
                [4, "3B"],
                [2, "CF"],
                [22, "C"],
            ],
            "bullpen": [45, 62, 53, 64, 41, 59, 54, 56, 43, 68, 55],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
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
                41: "John Lackey",
                # Bench
                18: "Shane Victorino",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
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
            ],
            "bullpen": [63, 40, 30, 31, 59, 36, 11, 51, 19, 22, 46],
        },
        "umpires": {
            "HP": "Jordan Baker",
            "1B": "Tim McClelland",
            "2B": "Jerry Meals",
            "3B": "Marvin Hudson",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. HOU #19 Robbie Grossman (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b c s")
t1.out("K")

# 2. HOU #27 Jose Altuve (X - X - X)
t1.new_ab()
t1.pitch_list("f b b")
t1.out("G6-3")

# 3. HOU #15 Jason Castro (X - X - X)
t1.new_ab()
t1.pitch_list("b c t b b f f f d")
t1.reach("BB")
t1.advance(2, "12 BB")
t1.advance(4, "13 1B")

# 4. HOU #12 Carlos Pena (X - X - 15)
t1.new_ab()
t1.pitch_list("b c b b b")
t1.reach("BB")
t1.advance(3, "13 1B")

# 5. HOU #13 Ronny Cedeno (X - 15 - 12)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1, rbis=1)

# 6. HOU #21 Fernando Martinez (12 - X - 13)
t1.new_ab()
t1.pitch_list("1")
t1.out("F9")


# Bot 1st
# Pitching: HOU #20 Bud Norris
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G3")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f")
b1.hit(2)
b1.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - 29 - X)
b1.new_ab()
b1.pitch_list("b c b b b")
b1.reach("BB")
b1.advance(2, "34 1B")
b1.advance(3, "37 BB")

# 4. BOS #34 David Ortiz (X - 29 - 15)
b1.new_ab()
b1.pitch_list("f s b f f")
b1.hit(1, rbis=1)
b1.advance(2, "37 BB")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
b1.new_ab()
b1.pitch_list("c b b f b s")
b1.out("K")

# 6. BOS #37 Mike Carp (X - 15 - 34)
b1.new_ab()
b1.pitch_list("b b b c f b")
b1.reach("BB")

# 7. BOS #39 Jarrod Saltalamacchia (15 - 34 - 37)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 7. HOU #30 Matt Dominguez (X - X - X)
t2.new_ab()
t2.pitch_list("c b b")
t2.hit(1)
t2.advance(2, "9 G5-3")

# 8. HOU #28 Rick Ankiel (X - X - 30)
t2.new_ab()
t2.out("F9")

# 9. HOU #9  Marwin Gonzalez (X - X - 30)
t2.new_ab()
t2.pitch_list("c b 1 f")
t2.out("G5-3")

# 1. HOU #19 Robbie Grossman (X - 30 - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("F9")


# Bot 2nd
# Pitching: HOU #20 Bud Norris
b2 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("c b c")
b2.hit(1)
b2.thrown_out(2, "2 FC6-4", 2, 20)

# 9. BOS #7  Stephen Drew (X - X - 16)
b2.new_ab()
b2.pitch_list("b c c t")
b2.out("KT")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b2.new_ab()
b2.pitch_list("1 c f")
b2.reach("FC6-4")
b2.thrown_out(2, "29 CS", 3, 20)

# 2. BOS #29 Daniel Nava (X - X - 2)
b2.new_ab()
b2.pitch_list("c b 1 b")
b2.no_ab("CS")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 2. HOU #27 Jose Altuve (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 3. HOU #15 Jason Castro (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G4-3")

# 4. HOU #12 Carlos Pena (X - X - X)
t3.new_ab()
t3.pitch_list("c b f s")
t3.out("K")


# Bot 3rd
# Pitching: HOU #20 Bud Norris
b3 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("f c s")
b3.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c f f")
b3.out("F8")

# 4. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 5. HOU #13 Ronny Cedeno (X - X - X)
t4.new_ab()
t4.out("L9")

# 6. HOU #21 Fernando Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c f b f c")
t4.out("!K")

# 7. HOU #30 Matt Dominguez (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("F8")


# Bot 4th
# Pitching: HOU #20 Bud Norris
b4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("c s")
b4.hit(1)
b4.thrown_out(2, "9-6", 1, 20)

# 6. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("s")
b4.hit(1)
b4.advance(3, "39 1B")
b4.advance(4, "7 3B")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.advance(4, "7 3B")

# 8. BOS #16 Will Middlebrooks (37 - X - 39)
b4.new_ab()
b4.pitch_list("f c b b s")
b4.out("K")

# 9. BOS #7  Stephen Drew (37 - X - 39)
b4.new_ab()
b4.pitch_list("f b 1 s f")
b4.hit(3, rbis=2)

# 1. BOS #2  Jacoby Ellsbury (7 - X - X)
b4.new_ab()
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 8. HOU #28 Rick Ankiel (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G5-3")

# 9. HOU #9  Marwin Gonzalez (X - X - X)
t5.new_ab()
t5.pitch_list("b b c f f b f")
t5.out("G3-1")

# 1. HOU #19 Robbie Grossman (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G3-1")


# Bot 5th
# Pitching: HOU #20 Bud Norris
b5 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.error(6)
b5.reach("E6")
b5.error(6)
b5.advance(2, "E6")
b5.advance("U", "15 2B")

# 3. BOS #15 Dustin Pedroia (X - 29 - X)
b5.new_ab()
b5.hit(2, rbis=1)
b5.advance("U", "37 2B")

# 4. BOS #34 David Ortiz (X - 15 - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("F7")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b5.new_ab()
b5.pitch_list("c b c f s")
b5.out("K")

# 6. BOS #37 Mike Carp (X - 15 - X)
b5.new_ab()
b5.hit(2, rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
b5.new_ab()
b5.pitch_list("f f f d")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 2. HOU #27 Jose Altuve (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G3")

# 3. HOU #15 Jason Castro (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.hit(1)
t6.advance(2, "12 1B")
t6.advance(3, "13 1B")

# 4. HOU #12 Carlos Pena (X - X - 15)
t6.new_ab()
t6.hit(1)
t6.advance(2, "13 1B")

# 5. HOU #13 Ronny Cedeno (X - 15 - 12)
t6.new_ab()
t6.pitch_list("c f f b")
t6.hit(1)
t6.thrown_out(2, "30 FC6-4", 3, 41)

# 6. HOU #21 Fernando Martinez (15 - 12 - 13)
t6.new_ab()
t6.pitch_list("b f f s")
t6.out("K")

# 7. HOU #30 Matt Dominguez (15 - 12 - 13)
t6.new_ab()
t6.reach("FC6-4")


# Bot 6th
# Pitching: HOU #20 Bud Norris
b6 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("b s c b")
b6.out("L5")

# 9. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("f s f b b b")
b6.out("(F)P5")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b b f f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #59 Clayton Mortensen
t7 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #41 John Lackey
t7.pitching_substitution(59)

# 8. HOU #28 Rick Ankiel (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("P4")

# 9. HOU #9  Marwin Gonzalez (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.error(1)
t7.reach("E1")
t7.thrown_out(2, "19 FC4-6", 2, 59)

# 1. HOU #19 Robbie Grossman (X - X - 9)
t7.new_ab()
t7.pitch_list("c b b c b")
t7.reach("FC4-6")

# 2. HOU #27 Jose Altuve (X - X - 19)
t7.new_ab()
t7.pitch_list("s")
t7.out("G4-3")


# Bot 7th
# Pitching: HOU #68 José Cisnero
b7 = game.new_inning()

# Pitching change (HOU): #68 José Cisnero replaces #20 Bud Norris
b7.pitching_substitution(68)

# 2. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c b f")
b7.hit(1)
b7.advance(2, "15 BLK")
b7.advance(4, "34 2B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b7.new_ab()
b7.pitch_list("b b n c f f")
b7.balk()
b7.out("L5")

# 4. BOS #34 David Ortiz (X - 29 - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2, rbis=1)

# 5. BOS #12 Mike Napoli (X - 34 - X)
b7.new_ab()
b7.pitch_list("b c c d s")
b7.out("K")

# 6. BOS #37 Mike Carp (X - 34 - X)
b7.new_ab()
b7.pitch_list("c b c c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #59 Clayton Mortensen
t8.pitching_substitution(19)

# Defensive change (BOS): #5 Jonny Gomes replaces #37 Mike Carp (LF), playing LF, batting 6th
t8.defensive_substitution(6, 5, "7")

# 3. HOU #15 Jason Castro (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("F7")

# 4. HOU #12 Carlos Pena (X - X - X)
t8.new_ab()
t8.pitch_list("c c")
t8.hit(1)
t8.advance(2, "21 WP")

# 5. HOU #13 Ronny Cedeno (X - X - 12)
t8.new_ab()
t8.pitch_list("t c")
t8.out("F8")

# 6. HOU #21 Fernando Martinez (X - X - 12)
t8.new_ab()
t8.pitch_list("c s b f")
t8.wp()
t8.out("G4-3")


# Bot 8th
# Pitching: HOU #68 José Cisnero
b8 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("c b s b s")
b8.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("b b f")
b8.out("F9")

# 9. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("c c f b f")
b8.out("P6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
t9.pitching_substitution(40)

# 7. HOU #30 Matt Dominguez (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.out("F7")

# 8. HOU #28 Rick Ankiel (X - X - X)
t9.new_ab()
t9.pitch_list("b b f f f")
t9.hit(2)
t9.advance(3, "9 F8")

# 9. HOU #9  Marwin Gonzalez (X - 28 - X)
t9.new_ab()
t9.out("F8")

# 1. HOU #19 Robbie Grossman (28 - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F9")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41)

# Loser team: HOU
# LP: HOU #20 Bud Norris
game.losing_pitcher(20, is_away_team=True)

# print(game)
game.generate_scorecard()
