import os
from baseball_scorecard.baseball_scorecard import Scorecard

# AZ @ BOS, 2013-08-03
# https://www.baseball-reference.com/boxes/BOS/BOS201308030.shtml
# https://www.mlb.com/gameday/d-backs-vs-red-sox/2013/08/03/348382/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-03 19:12-22:14",
        "at": "Fenway Park, Boston, MA",
        "att": "37,941",
        "temp": "80F, Partly Cloudy",
        "wind": "13mph, Out To CF",
        "away": {
            "team": "Arizona Diamondbacks",
            "starter": 46,
            "roster": {
                # Lineup
                8: "Gerardo Parra",
                2: "Aaron Hill",
                44: "Paul Goldschmidt",
                12: "Eric Chavez",
                14: "Martín Prado",
                7: "Cody Ross",
                13: "Jason Kubel",
                27: "Wil Nieves",
                4: "Cliff Pennington",
                # Starting pitcher
                46: "Patrick Corbin",
                # Bench
                6: "Adam Eaton",
                54: "Tuffy Gosewisch",
                11: "AJ Pollock",
                1: "Didi Gregorius",
                # Bullpen
                40: "J.J. Putz",
                38: "Will Harris",
                36: "Wade Miley",
                30: "David Hernandez",
                52: "Zeke Spruill",
                48: "Randall Delgado",
                55: "Josh Collmenter",
                21: "Heath Bell",
                49: "Tony Sipp",
                29: "Brad Ziegler",
                54: "Joe Thatcher",
            },
            "lefties": [46, 36, 49, 54],
            "lineup": [
                [8, "8"],
                [2, "4"],
                [44, "3"],
                [12, "0"],
                [14, "5"],
                [7, "9"],
                [13, "7"],
                [27, "2"],
                [4, "6"],
            ],
            "bench": [
                [6, "CF"],
                [54, "C"],
                [11, "CF"],
                [1, "SS"],
            ],
            "bullpen": [40, 38, 36, 30, 52, 48, 55, 21, 49, 29, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                23: "Brandon Snyder",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                37: "Mike Carp",
                26: "Brock Holt",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
                # Bullpen
                35: "Steven Wright",
                41: "John Lackey",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [23, "5"],
            ],
            "bench": [
                [37, "1B"],
                [26, "2B"],
                [29, "LF"],
                [20, "C"],
            ],
            "bullpen": [35, 41, 32, 66, 31, 36, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Eric Cooper",
            "1B": "Paul Schrieber",
            "2B": "Chad Fairchild",
            "3B": "Jeff Kellogg",
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
# Pitching: BOS #44 Jake Peavy
t1 = game.new_inning()

# 1. AZ #8  Gerardo Parra (X - X - X)
t1.new_ab()
t1.pitch_list("t")
t1.out("F8")

# 2. AZ #2  Aaron Hill (X - X - X)
t1.new_ab()
t1.pitch_list("b c s s")
t1.out("K")

# 3. AZ #44 Paul Goldschmidt (X - X - X)
t1.new_ab()
t1.pitch_list("b c b b b")
t1.reach("BB")
t1.thrown_out(2, "12 CS", 3, 44)

# 4. AZ #12 Eric Chavez (X - X - 44)
t1.new_ab()
t1.pitch_list("c b")
t1.no_ab("CS")


# Bot 1st
# Pitching: AZ #46 Patrick Corbin
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c c s")
b1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b f f b f")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #44 Jake Peavy
t2 = game.new_inning()

# 4. AZ #12 Eric Chavez (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("P5")

# 5. AZ #14 Martín Prado (X - X - X)
t2.new_ab()
t2.pitch_list("c s b b b b")
t2.reach("BB")

# 6. AZ #7  Cody Ross (X - X - 14)
t2.new_ab()
t2.pitch_list("b")
t2.out("F8")

# 7. AZ #13 Jason Kubel (X - X - 14)
t2.new_ab()
t2.pitch_list("c b c s")
t2.out("K")


# Bot 2nd
# Pitching: AZ #46 Patrick Corbin
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b")
b2.hit(1)
b2.advance(2, "12 WP")
b2.error(4)
b2.advance(3, "39 E4")

# 5. BOS #12 Mike Napoli (X - X - 34)
b2.new_ab(is_risp=True)
b2.pitch_list("c b b b f b")
b2.wp()
b2.reach("BB")
b2.advance(2, "39 E4")

# 6. BOS #5  Jonny Gomes (X - 34 - 12)
b2.new_ab(is_risp=True)
b2.pitch_list("b c c s")
b2.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - 34 - 12)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.reach("FC4")

# 8. BOS #7  Stephen Drew (34 - 12 - 39)
b2.new_ab(is_risp=True)
b2.pitch_list("c c s")
b2.out("K")

# 9. BOS #23 Brandon Snyder (34 - 12 - 39)
b2.new_ab(is_risp=True)
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #44 Jake Peavy
t3 = game.new_inning()

# 8. AZ #27 Wil Nieves (X - X - X)
t3.new_ab()
t3.pitch_list("b s f f")
t3.hit(1)

# 9. AZ #4  Cliff Pennington (X - X - 27)
t3.new_ab()
t3.pitch_list("f b f s")
t3.out("K")

# 1. AZ #8  Gerardo Parra (X - X - 27)
t3.new_ab()
t3.pitch_list("b 1")
t3.out("(F)P5")

# 2. AZ #2  Aaron Hill (X - X - 27)
t3.new_ab()
t3.pitch_list("1 c b d c s")
t3.out("K")


# Bot 3rd
# Pitching: AZ #46 Patrick Corbin
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("c b f s")
b3.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(1)
b3.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.pitch_list("c b d 1 b")
b3.hit(1)

# 4. BOS #34 David Ortiz (X - 18 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("f f d s")
b3.out("K")

# 5. BOS #12 Mike Napoli (X - 18 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("f b c f")
b3.out("P6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #44 Jake Peavy
t4 = game.new_inning()

# 3. AZ #44 Paul Goldschmidt (X - X - X)
t4.new_ab()
t4.pitch_list("s f")
t4.hit(4)

# 4. AZ #12 Eric Chavez (X - X - X)
t4.new_ab()
t4.pitch_list("f c")
t4.out("G3-1")

# 5. AZ #14 Martín Prado (X - X - X)
t4.new_ab()
t4.pitch_list("b c b c")
t4.out("F9")

# 6. AZ #7  Cody Ross (X - X - X)
t4.new_ab()
t4.pitch_list("b c f")
t4.out("F9")


# Bot 4th
# Pitching: AZ #46 Patrick Corbin
b4 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.out("F9")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s b")
b4.hit(1)

# 9. BOS #23 Brandon Snyder (X - X - 7)
b4.new_ab()
b4.pitch_list("1 c s s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #44 Jake Peavy
t5 = game.new_inning()

# 7. AZ #13 Jason Kubel (X - X - X)
t5.new_ab()
t5.pitch_list("f f f s")
t5.out("K")

# 8. AZ #27 Wil Nieves (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 9. AZ #4  Cliff Pennington (X - X - X)
t5.new_ab()
t5.pitch_list("c b c b b s")
t5.out("K")


# Bot 5th
# Pitching: AZ #46 Patrick Corbin
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("f b s")
b5.out("L8")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.out("G3-1")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #44 Jake Peavy
t6 = game.new_inning()

# 1. AZ #8  Gerardo Parra (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b b s")
t6.out("K")

# 2. AZ #2  Aaron Hill (X - X - X)
t6.new_ab()
t6.pitch_list("s b b")
t6.hit(1)

# 3. AZ #44 Paul Goldschmidt (X - X - 2)
t6.new_ab()
t6.pitch_list("b")
t6.out("L9")

# 4. AZ #12 Eric Chavez (X - X - 2)
t6.new_ab()
t6.pitch_list("1 d 1 c f f f")
t6.out("(F)P6")


# Bot 6th
# Pitching: AZ #46 Patrick Corbin
b6 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("s f b f b b b")
b6.reach("BB")
b6.thrown_out(2, "39 DP5-4-3", 2, 46)

# 6. BOS #5  Jonny Gomes (X - X - 12)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b6.new_ab()
b6.pitch_list("b b")
b6.out("DP5-4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #44 Jake Peavy
t7 = game.new_inning()

# 5. AZ #14 Martín Prado (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G6-3")

# 6. AZ #7  Cody Ross (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")

# 7. AZ #13 Jason Kubel (X - X - X)
t7.new_ab()
t7.pitch_list("c f b b b")
t7.out("G3-1")


# Bot 7th
# Pitching: AZ #46 Patrick Corbin
b7 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("s")
b7.hit(1)
b7.advance(3, "23 1B")
b7.advance(4, "2 1B")

# 9. BOS #23 Brandon Snyder (X - X - 7)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1)
# Offensive change (BOS): Pinch-runner #26 Brock Holt replaces #23 Brandon Snyder
b7.offensive_substitution(9, 26, "PR")
b7.atbase("PR")
b7.advance(2, "2 WP")
b7.advance(3, "2 1B")
b7.advance(4, "18 SF8")

# 1. BOS #2  Jacoby Ellsbury (7 - X - 23)
b7.new_ab(is_risp=True)
b7.pitch_list("f b 1 s b")
b7.wp()
b7.hit(1, rbis=1)
b7.advance(2, "15 SB")

# Pitching change (AZ): #38 Will Harris replaces #46 Patrick Corbin
b7.pitching_substitution(38)

# 2. BOS #18 Shane Victorino (26 - X - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("c s f b f")
b7.out("SF8", rbis=1)

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b7.new_ab()
b7.pitch_list("1 b b 1 b c f f s")
b7.out("K")

# Pitching change (AZ): #54 Joe Thatcher replaces #38 Will Harris
b7.pitching_substitution(54)

# 4. BOS #34 David Ortiz (X - 2 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.out("P4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #44 Jake Peavy
t8 = game.new_inning()

# Defensive switch (BOS): #26 Brock Holt moves to 3B
t8.defensive_switch(26, "5")

# 8. AZ #27 Wil Nieves (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.advance(2, "4 HBP")
t8.advance(3, "8 1B")
t8.advance(4, "2 1B")

# Pitching change (BOS): #32 Craig Breslow replaces #44 Jake Peavy
t8.pitching_substitution(32)

# 9. AZ #4  Cliff Pennington (X - X - 27)
t8.new_ab()
t8.pitch_list("f c")
t8.reach("HBP")
t8.advance(2, "8 1B")
t8.advance(3, "2 1B")
t8.thrown_out(4, "2 7-2", 1, 36)

# 1. AZ #8  Gerardo Parra (X - 27 - 4)
t8.new_ab(is_risp=True)
t8.pitch_list("l l b")
t8.hit(1)
t8.advance(2, "2 7-2")

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
t8.pitching_substitution(36)

# 2. AZ #2  Aaron Hill (27 - 4 - 8)
t8.new_ab(is_risp=True)
t8.hit(1, rbis=1)

# 3. AZ #44 Paul Goldschmidt (X - 8 - 2)
t8.new_ab(is_risp=True)
t8.pitch_list("b f f 2 t")
t8.out("KT")

# 4. AZ #12 Eric Chavez (X - 8 - 2)
t8.new_ab(is_risp=True)
t8.out("L7")


# Bot 8th
# Pitching: AZ #30 David Hernandez
b8 = game.new_inning()

# Pitching change (AZ): #30 David Hernandez replaces #54 Joe Thatcher
b8.pitching_substitution(30)

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("b f c b f b b")
b8.reach("BB")
b8.advance(4, "39 HR")

# 6. BOS #5  Jonny Gomes (X - X - 12)
b8.new_ab()
b8.pitch_list("c f b c")
b8.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b8.new_ab()
b8.pitch_list("s")
b8.hit(4, rbis=2)

# Pitching change (AZ): #49 Tony Sipp replaces #30 David Hernandez
b8.pitching_substitution(49)

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("b b c s b c")
b8.out("!K")

# 9. BOS #26 Brock Holt (X - X - X)
b8.new_ab()
b8.pitch_list("s")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# 5. AZ #14 Martín Prado (X - X - X)
t9.new_ab()
t9.pitch_list("b t s b b b")
t9.reach("BB")
t9.thrown_out(2, "7 FC4-6", 1, 19)

# 6. AZ #7  Cody Ross (X - X - 14)
t9.new_ab()
t9.pitch_list("f b b t 1")
t9.reach("FC4-6")
t9.thrown_out(2, "13 DP6-4-3", 2, 19)

# 7. AZ #13 Jason Kubel (X - X - 7)
t9.new_ab()
t9.pitch_list("b s b f")
t9.out("DP6-4-3")

# Winning team: BOS
# WP: BOS #44 Jake Peavy
game.winning_pitcher(44)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: AZ
# LP: AZ #46 Patrick Corbin
game.losing_pitcher(46, is_away_team=True)

# print(game)
game.generate_scorecard()
