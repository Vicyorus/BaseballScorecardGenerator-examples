import os
from baseball_scorecard.baseball_scorecard import Scorecard

# HOU @ BOS, 2013-04-26
# https://www.baseball-reference.com/boxes/BOS/BOS201304260.shtml
# https://www.mlb.com/gameday/astros-vs-red-sox/2013/04/26/347081/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-26 19:09-22:58",
        "at": "Fenway Park, Boston, MA",
        "att": "29,312",
        "temp": "47F, Partly Cloudy",
        "wind": "8mph, Out To RF",
        "away": {
            "team": "Houston Astros",
            "starter": 45,
            "roster": {
                # Lineup
                19: "Robbie Grossman",
                27: "Jose Altuve",
                15: "Jason Castro",
                4: "Brandon Laird",
                12: "Carlos Pena",
                23: "Chris Carter",
                21: "Fernando Martinez",
                30: "Matt Dominguez",
                9: "Marwin Gonzalez",
                # Starting pitcher
                45: "Erik Bedard",
                # Bench
                13: "Ronny Cedeno",
                2: "Brandon Barnes",
                22: "Carlos Corporán",
                28: "Rick Ankiel",
                # Bullpen
                62: "Hector Ambriz",
                53: "Wesley Wright",
                20: "Bud Norris",
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
                [4, "3"],
                [12, "0"],
                [23, "7"],
                [21, "9"],
                [30, "5"],
                [9, "6"],
            ],
            "bench": [
                [13, "SS"],
                [2, "CF"],
                [22, "C"],
                [28, "CF"],
            ],
            "bullpen": [62, 53, 20, 64, 41, 59, 54, 56, 43, 68, 55],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                18: "Shane Victorino",
                20: "Ryan Lavarnway",
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
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [16, "5"],
                [3, "2"],
                [23, "6"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [37, "1B"],
                [18, "CF"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 30, 31, 59, 36, 11, 51, 19, 22],
        },
        "umpires": {
            "HP": "Jerry Meals",
            "1B": "Marvin Hudson",
            "2B": "Jordan Baker",
            "3B": "Tim McClelland",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. HOU #19 Robbie Grossman (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("L4")

# 2. HOU #27 Jose Altuve (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(2)
t1.error(1)
t1.advance(3, "4 POE1")

# 3. HOU #15 Jason Castro (X - 27 - X)
t1.new_ab()
t1.pitch_list("s b b f s")
t1.out("K")

# 4. HOU #4  Brandon Laird (X - 27 - X)
t1.new_ab()
t1.pitch_list("f b s f f f 2 f s")
t1.out("K")


# Bot 1st
# Pitching: HOU #45 Erik Bedard
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c s b b b f")
b1.hit(1)
b1.advance(4, "15 2B")

# 2. BOS #5  Jonny Gomes (X - X - 2)
b1.new_ab()
b1.pitch_list("b 1 c s b f c")
b1.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b1.new_ab()
b1.pitch_list("b b f 1 c b")
b1.hit(2, rbis=1)

# 4. BOS #34 David Ortiz (X - 15 - X)
b1.new_ab()
b1.pitch_list("b d s s s")
b1.out("K")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b1.new_ab()
b1.pitch_list("c f b f d f f b")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. HOU #12 Carlos Pena (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c f s")
t2.out("K")

# 6. HOU #23 Chris Carter (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b f s")
t2.out("K")

# 7. HOU #21 Fernando Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")


# Bot 2nd
# Pitching: HOU #45 Erik Bedard
b2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b c f")
b2.out("F8")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("f b s f b f f")
b2.out("P5")

# 8. BOS #3  David Ross (X - X - X)
b2.new_ab()
b2.pitch_list("s c b")
b2.hit(4)

# 9. BOS #23 Pedro Ciriaco (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(3)

# 1. BOS #2  Jacoby Ellsbury (23 - X - X)
b2.new_ab()
b2.pitch_list("b b l f")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 8. HOU #30 Matt Dominguez (X - X - X)
t3.new_ab()
t3.pitch_list("c b b c b")
t3.hit(2)
t3.advance(3, "9 F8")
t3.advance(4, "19 G4-3")

# 9. HOU #9  Marwin Gonzalez (X - 30 - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F8")

# 1. HOU #19 Robbie Grossman (30 - X - X)
t3.new_ab()
t3.pitch_list("b 3")
t3.out("G4-3", rbis=1)

# 2. HOU #27 Jose Altuve (X - X - X)
t3.new_ab()
t3.pitch_list("b c b c b")
t3.out("L8")


# Bot 3rd
# Pitching: HOU #45 Erik Bedard
b3 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("f s s")
b3.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(2)
b3.advance(4, "12 2B")

# 4. BOS #34 David Ortiz (X - 15 - X)
b3.new_ab()
b3.pitch_list("b c b f s")
b3.out("K")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b3.new_ab()
b3.pitch_list("d s f b f")
b3.hit(2, rbis=1)

# 6. BOS #29 Daniel Nava (X - 12 - X)
b3.new_ab()
b3.pitch_list("c s b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 3. HOU #15 Jason Castro (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(2)

# 4. HOU #4  Brandon Laird (X - 15 - X)
t4.new_ab()
t4.pitch_list("c c s")
t4.out("K")

# 5. HOU #12 Carlos Pena (X - 15 - X)
t4.new_ab()
t4.pitch_list("s b s c")
t4.out("!K")

# 6. HOU #23 Chris Carter (X - 15 - X)
t4.new_ab()
t4.pitch_list("b b s b c b")
t4.reach("BB")

# 7. HOU #21 Fernando Martinez (X - 15 - 23)
t4.new_ab()
t4.pitch_list("b s f s")
t4.out("K")


# Bot 4th
# Pitching: HOU #45 Erik Bedard
b4 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c f f f f")
b4.hit(4)

# 8. BOS #3  David Ross (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.hit(4)

# Pitching change (HOU): #56 Paul Clemens replaces #45 Erik Bedard
b4.pitching_substitution(56)

# 9. BOS #23 Pedro Ciriaco (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b")
b4.out("L7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b4.new_ab()
b4.out("G4-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s b f f")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 8. HOU #30 Matt Dominguez (X - X - X)
t5.new_ab()
t5.pitch_list("b b c")
t5.hit(2)
t5.advance(3, "19 WP")
t5.advance(4, "27 SF9")

# 9. HOU #9  Marwin Gonzalez (X - 30 - X)
t5.new_ab()
t5.pitch_list("c f b s")
t5.out("K")

# 1. HOU #19 Robbie Grossman (X - 30 - X)
t5.new_ab()
t5.pitch_list("c s b b b b")
t5.wp()
t5.reach("BB")

# 2. HOU #27 Jose Altuve (30 - X - 19)
t5.new_ab()
t5.pitch_list("b")
t5.out("SF9", rbis=1)

# 3. HOU #15 Jason Castro (X - X - 19)
t5.new_ab()
t5.pitch_list("b 1 c b 1")
t5.out("L7")


# Bot 5th
# Pitching: HOU #56 Paul Clemens
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c b b s")
b5.hit(4)

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("c b s c")
b5.out("!K")

# 6. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("c f b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 4. HOU #4  Brandon Laird (X - X - X)
t6.new_ab()
t6.pitch_list("b c b s s")
t6.out("K")

# 5. HOU #12 Carlos Pena (X - X - X)
t6.new_ab()
t6.pitch_list("b b f c b b")
t6.reach("BB")

# 6. HOU #23 Chris Carter (X - X - 12)
t6.new_ab()
t6.pitch_list("s c c")
t6.out("!K")

# 7. HOU #21 Fernando Martinez (X - X - 12)
t6.new_ab()
t6.pitch_list("b c")
t6.out("G5-3")


# Bot 6th
# Pitching: HOU #56 Paul Clemens
b6 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("c f b c")
b6.out("!K")

# 8. BOS #3  David Ross (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c c")
b6.hit(1)
b6.advance(3, "2 1B")

# 9. BOS #23 Pedro Ciriaco (X - X - 3)
b6.new_ab()
b6.pitch_list("b 1 s 1 b f b f 1 f 1 1")
b6.out("P6")

# 1. BOS #2  Jacoby Ellsbury (X - X - 3)
b6.new_ab()
b6.pitch_list("f b f b f")
b6.hit(1)
b6.advance(2, "5 SB")

# 2. BOS #5  Jonny Gomes (3 - X - 2)
b6.new_ab()
b6.pitch_list("c c b f d s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #59 Clayton Mortensen
t7 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #46 Ryan Dempster
t7.pitching_substitution(59)

# 8. HOU #30 Matt Dominguez (X - X - X)
t7.new_ab()
t7.pitch_list("c b c f")
t7.reach("HBP")
t7.error(3)
t7.advance(2, "9 1B")
t7.advance(3, "9 E3")
t7.advance(4, "27 SF9")

# 9. HOU #9  Marwin Gonzalez (X - X - 30)
t7.new_ab()
t7.hit(1)
t7.advance(2, "15 1B")

# 1. HOU #19 Robbie Grossman (30 - X - 9)
t7.new_ab()
t7.pitch_list("b 1 s b c b c")
t7.out("!K")

# Pitching change (BOS): #36 Junichi Tazawa replaces #59 Clayton Mortensen
t7.pitching_substitution(36)

# 2. HOU #27 Jose Altuve (30 - X - 9)
t7.new_ab()
t7.out("SF9", rbis=1)

# 3. HOU #15 Jason Castro (X - X - 9)
t7.new_ab()
t7.pitch_list("c f")
t7.hit(1)

# 4. HOU #4  Brandon Laird (X - 9 - 15)
t7.new_ab()
t7.pitch_list("c f b c")
t7.out("!K")


# Bot 7th
# Pitching: HOU #53 Wesley Wright
b7 = game.new_inning()

# Pitching change (HOU): #53 Wesley Wright replaces #56 Paul Clemens
b7.pitching_substitution(53)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b c f")
b7.hit(1)
b7.thrown_out(2, "34 DP6-3", 1, 53)

# 4. BOS #34 David Ortiz (X - X - 15)
b7.new_ab()
b7.pitch_list("f 1")
b7.out("DP6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2)

# 6. BOS #29 Daniel Nava (X - 12 - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t8.pitching_substitution(19)

# 5. HOU #12 Carlos Pena (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G1-3")

# 6. HOU #23 Chris Carter (X - X - X)
t8.new_ab()
t8.pitch_list("b c b")
t8.hit(2)
t8.advance(3, "21 G4-3")

# 7. HOU #21 Fernando Martinez (X - 23 - X)
t8.new_ab()
t8.pitch_list("b c s f f f")
t8.out("G4-3")

# 8. HOU #30 Matt Dominguez (23 - X - X)
t8.new_ab()
t8.pitch_list("c f f s")
t8.out("K")


# Bot 8th
# Pitching: HOU #55 Rhiner Cruz
b8 = game.new_inning()

# Pitching change (HOU): #55 Rhiner Cruz replaces #53 Wesley Wright
b8.pitching_substitution(55)

# 7. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("c c b b")
b8.hit(1)
b8.advance(2, "3 1B")
b8.advance(3, "23 1B")
b8.thrown_out(3, "2 DP6-5", 2, 55)

# 8. BOS #3  David Ross (X - X - 16)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)
b8.advance(2, "23 1B")
b8.advance(4, "5 1B")

# 9. BOS #23 Pedro Ciriaco (X - 16 - 3)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(1)
b8.advance(3, "5 1B")

# 1. BOS #2  Jacoby Ellsbury (16 - 3 - 23)
b8.new_ab()
b8.pitch_list("b c b f b f")
b8.out("DP6-5")

# 2. BOS #5  Jonny Gomes (X - 3 - 23)
b8.new_ab()
b8.hit(1, rbis=1)

# 3. BOS #15 Dustin Pedroia (23 - X - 5)
b8.new_ab()
b8.pitch_list("b 1 b b c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #63 Alex Wilson
t9 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #19 Koji Uehara
t9.pitching_substitution(63)

# 9. HOU #9  Marwin Gonzalez (X - X - X)
t9.new_ab()
t9.out("G4-3")

# 1. HOU #19 Robbie Grossman (X - X - X)
t9.new_ab()
t9.pitch_list("c b s c")
t9.out("!K")

# 2. HOU #27 Jose Altuve (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.out("F8")

# Winning team: BOS
# WP: BOS #46 Ryan Dempster
game.winning_pitcher(46)

# Loser team: HOU
# LP: HOU #45 Erik Bedard
game.losing_pitcher(45, is_away_team=True)

# print(game)
game.generate_scorecard()
