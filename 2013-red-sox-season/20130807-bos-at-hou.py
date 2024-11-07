import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ HOU, 2013-08-07
# https://www.baseball-reference.com/boxes/HOU/HOU201308070.shtml
# https://www.mlb.com/gameday/red-sox-vs-astros/2013/08/07/348438/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-07 20:09-00:02 +1",
        "at": "Minute Maid Park, Houston, TX",
        "att": "22,205",
        "temp": "73F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                26: "Brock Holt",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                54: "Pedro Beato",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
            },
            "lefties": [32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [5, "7"],
                [7, "6"],
                [39, "2"],
                [26, "5"],
            ],
            "bench": [
                [12, "1B"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 32, 66, 44, 31, 36, 19, 54, 62, 22],
        },
        "home": {
            "team": "Houston Astros",
            "starter": 48,
            "roster": {
                # Lineup
                19: "Robbie Grossman",
                2: "Brandon Barnes",
                27: "Jose Altuve",
                15: "Jason Castro",
                59: "Marc Krauss",
                29: "Brett Wallace",
                30: "Matt Dominguez",
                28: "L.J. Hoes",
                10: "Jake Elmore",
                # Starting pitcher
                48: "Jarred Cosart",
                # Bench
                23: "Chris Carter",
                22: "Carlos Corporán",
                6: "Jonathan Villar",
                # Bullpen
                45: "Erik Bedard",
                53: "Wesley Wright",
                39: "Brett Oberholtzer",
                63: "Chia-Jen Lo",
                64: "Lucas Harrell",
                35: "Josh Fields",
                67: "Jorge De Leon",
                54: "Travis Blackley",
                60: "Dallas Keuchel",
                41: "Brad Peacock",
                18: "Jordan Lyles",
                61: "Josh Zeid",
            },
            "lefties": [45, 53, 39, 54, 60],
            "lineup": [
                [19, "7"],
                [2, "8"],
                [27, "4"],
                [15, "2"],
                [59, "0"],
                [29, "3"],
                [30, "5"],
                [28, "9"],
                [10, "6"],
            ],
            "bench": [
                [23, "1B"],
                [22, "C"],
                [6, "2B"],
            ],
            "bullpen": [45, 53, 39, 63, 64, 35, 67, 54, 60, 41, 18, 61],
        },
        "umpires": {
            "HP": "Mark Carlson",
            "1B": "Gerry Davis",
            "2B": "Dan Iassogna",
            "3B": "Brian Knight",
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
# Pitching: HOU #48 Jarred Cosart
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b")
t1.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(2, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("c b s d 1")
t1.out("F9")

# 4. BOS #34 David Ortiz (X - X - 18)
t1.new_ab()
t1.pitch_list("s b f")
t1.hit(1)

# 5. BOS #37 Mike Carp (X - 18 - 34)
t1.new_ab(is_risp=True)
t1.pitch_list("b b b c c f")
t1.out("G1-3")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. HOU #19 Robbie Grossman (X - X - X)
b1.new_ab()
b1.pitch_list("b c f f b c")
b1.out("!K")

# 2. HOU #2  Brandon Barnes (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("G6-3")

# 3. HOU #27 Jose Altuve (X - X - X)
b1.new_ab()
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: HOU #48 Jarred Cosart
t2 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b b")
t2.reach("BB")
t2.advance(3, "39 2B")
t2.advance(4, "26 G4-3")

# 7. BOS #7  Stephen Drew (X - X - 5)
t2.new_ab()
t2.pitch_list("f b 1 f s")
t2.out("K")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 5)
t2.new_ab()
t2.pitch_list("c c b")
t2.hit(2)
t2.advance(3, "26 G4-3")

# 9. BOS #26 Brock Holt (5 - 39 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c b")
t2.out("G4-3", rbis=1)

# 1. BOS #2  Jacoby Ellsbury (39 - X - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b")
t2.out("L9")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 4. HOU #15 Jason Castro (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b f f s")
b2.out("K")

# 5. HOU #59 Marc Krauss (X - X - X)
b2.new_ab()
b2.pitch_list("c b s b b c")
b2.out("!K")

# 6. HOU #29 Brett Wallace (X - X - X)
b2.new_ab()
b2.pitch_list("s b b s")
b2.hit(1)

# 7. HOU #30 Matt Dominguez (X - X - 29)
b2.new_ab()
b2.pitch_list("c")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: HOU #48 Jarred Cosart
t3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1)
t3.advance(3, "34 1B")
t3.advance(4, "37 DP3-6")

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.thrown_out(2, "37 DP3-6", 3, 48)

# 5. BOS #37 Mike Carp (15 - X - 34)
t3.new_ab(is_risp=True)
t3.out("DP3-6")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 8. HOU #28 L.J. Hoes (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G1-3")

# 9. HOU #10 Jake Elmore (X - X - X)
b3.new_ab()
b3.pitch_list("c b b c")
b3.hit(2)
b3.advance(4, "19 HR")

# 1. HOU #19 Robbie Grossman (X - 10 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f b c")
b3.hit(4, rbis=2)

# 2. HOU #2  Brandon Barnes (X - X - X)
b3.new_ab()
b3.pitch_list("b f b s")
b3.out("G6-3")

# 3. HOU #27 Jose Altuve (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: HOU #48 Jarred Cosart
t4 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("c f f b c")
t4.out("!K")

# 7. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("b c b")
t4.out("F9")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.advance(2, "26 BB")

# 9. BOS #26 Brock Holt (X - X - 39)
t4.new_ab()
t4.pitch_list("b b b c b")
t4.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - 39 - 26)
t4.new_ab(is_risp=True)
t4.pitch_list("b c c b c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 4. HOU #15 Jason Castro (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(1)
b4.thrown_out(2, "59 DP3-6-1", 1, 46)

# 5. HOU #59 Marc Krauss (X - X - 15)
b4.new_ab()
b4.pitch_list("b")
b4.out("DP3-6-1")

# 6. HOU #29 Brett Wallace (X - X - X)
b4.new_ab()
b4.pitch_list("c s s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: HOU #48 Jarred Cosart
t5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("b f b")
t5.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")
t5.advance(3, "34 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
t5.new_ab()
t5.pitch_list("c b 1 b f")
t5.hit(1)
t5.thrown_out(2, "37 DP4-6-3", 2, 48)

# 5. BOS #37 Mike Carp (15 - X - 34)
t5.new_ab(is_risp=True)
t5.pitch_list("c b b")
t5.out("DP4-6-3")


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 7. HOU #30 Matt Dominguez (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("G1-3")

# 8. HOU #28 L.J. Hoes (X - X - X)
b5.new_ab()
b5.pitch_list("s")
b5.out("L9")

# 9. HOU #10 Jake Elmore (X - X - X)
b5.new_ab()
b5.pitch_list("c b c f f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: HOU #48 Jarred Cosart
t6 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(2, "7 WP")
t6.advance(3, "26 BB")

# 7. BOS #7  Stephen Drew (X - X - 5)
t6.new_ab(is_risp=True)
t6.pitch_list("c b f b b d")
t6.wp()
t6.reach("BB")
t6.advance(2, "26 BB")

# Pitching change (HOU): #53 Wesley Wright replaces #48 Jarred Cosart
t6.pitching_substitution(53)

# 8. BOS #39 Jarrod Saltalamacchia (X - 5 - 7)
t6.new_ab(is_risp=True)
t6.pitch_list("c s s")
t6.out("K")

# 9. BOS #26 Brock Holt (X - 5 - 7)
t6.new_ab(is_risp=True)
t6.pitch_list("c b c f b b b")
t6.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (5 - 7 - 26)
t6.new_ab(is_risp=True)
t6.pitch_list("c f b b f c")
t6.out("!K")

# Pitching change (HOU): #61 Josh Zeid replaces #53 Wesley Wright
t6.pitching_substitution(61)

# 2. BOS #18 Shane Victorino (5 - 7 - 26)
t6.new_ab(is_risp=True)
t6.pitch_list("d c f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #46 Ryan Dempster
b6 = game.new_inning()

# 1. HOU #19 Robbie Grossman (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.hit(2)
b6.advance(3, "2 WP")
b6.advance(4, "27 1B")

# 2. HOU #2  Brandon Barnes (X - 19 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b s b s f b s")
b6.wp()
b6.out("K")

# 3. HOU #27 Jose Altuve (19 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b s")
b6.hit(1, rbis=1)
b6.advance(4, "15 2B")

# 4. HOU #15 Jason Castro (X - X - 27)
b6.new_ab()
b6.pitch_list("1 b 1 1 c")
b6.hit(2, rbis=1)
b6.advance(3, "T")
b6.advance(4, "59 SF9")

# 5. HOU #59 Marc Krauss (15 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f")
b6.out("SF9", rbis=1)

# 6. HOU #29 Brett Wallace (X - X - X)
b6.new_ab()
b6.pitch_list("c f b f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: HOU #61 Josh Zeid
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.out("L8")

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b c f")
t7.out("L3")

# 5. BOS #37 Mike Carp (X - X - X)
t7.new_ab()
t7.pitch_list("c b c")
t7.hit(1)
t7.advance(4, "5 HR")

# 6. BOS #5  Jonny Gomes (X - X - 37)
t7.new_ab()
t7.pitch_list("c")
t7.hit(4, rbis=2)

# Pitching change (HOU): #54 Travis Blackley replaces #61 Josh Zeid
t7.pitching_substitution(54)

# 7. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("b f c b b")
t7.hit(1)
t7.advance(2, "39 BB")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 7)
t7.new_ab()
t7.pitch_list("f f b b 1 b 1 b")
t7.reach("BB")

# Pitching change (HOU): #63 Chia-Jen Lo replaces #54 Travis Blackley
t7.pitching_substitution(63)

# Offensive change (BOS): Pinch-hitter #23 Brandon Snyder replaces #26 Brock Holt, batting 9th
t7.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Brandon Snyder (X - 7 - 39)
t7.new_ab(is_risp=True)
t7.pitch_list("s b b b f f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #46 Ryan Dempster
b7.pitching_substitution(36)

# Defensive change (BOS): #12 Mike Napoli replaces #18 Shane Victorino (RF), playing 1B, batting 2nd
b7.defensive_substitution(2, 12, "3")

# Defensive switch (BOS): #37 Mike Carp moves to LF
b7.defensive_switch(37, "7")

# Defensive switch (BOS): #5 Jonny Gomes moves to RF
b7.defensive_switch(5, "9")

# Defensive switch (BOS): #23 Brandon Snyder moves to 3B
b7.defensive_switch(23, "5")

# 7. HOU #30 Matt Dominguez (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("(F)F9")

# 8. HOU #28 L.J. Hoes (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F9")

# 9. HOU #10 Jake Elmore (X - X - X)
b7.new_ab()
b7.pitch_list("c c s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: HOU #63 Chia-Jen Lo
t8 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("f c f b f")
t8.out("(F)P2")

# 2. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("P3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("G1-3")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# 1. HOU #19 Robbie Grossman (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("L9")

# 2. HOU #2  Brandon Barnes (X - X - X)
b8.new_ab()
b8.pitch_list("f f b s")
b8.out("K")

# 3. HOU #27 Jose Altuve (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: HOU #35 Josh Fields
t9 = game.new_inning()

# Pitching change (HOU): #35 Josh Fields replaces #63 Chia-Jen Lo
t9.pitching_substitution(35)

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
# Offensive change (BOS): Pinch-runner #66 Drake Britton replaces #34 David Ortiz
t9.offensive_substitution(4, 66, "PR")
t9.atbase("PR")
t9.advance(2, "5 BB")
t9.advance(4, "7 HR")

# 5. BOS #37 Mike Carp (X - X - 34)
t9.new_ab()
t9.pitch_list("b b s c b")
t9.out("L7")

# 6. BOS #5  Jonny Gomes (X - X - 66)
t9.new_ab()
t9.pitch_list("b b c c d b")
t9.reach("BB")
t9.advance(4, "7 HR")

# 7. BOS #7  Stephen Drew (X - 66 - 5)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.hit(4, rbis=3)

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("c b c b")
t9.out("G6-3")

# 9. BOS #23 Brandon Snyder (X - X - X)
t9.new_ab()
t9.pitch_list("f s b b b s")
t9.out("K")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b9.pitching_substitution(19)

# Defensive switch (BOS): #66 Drake Britton moves to DH
b9.defensive_switch(66, "0")

# 4. HOU #15 Jason Castro (X - X - X)
b9.new_ab()
b9.pitch_list("s c t")
b9.out("KT")

# 5. HOU #59 Marc Krauss (X - X - X)
b9.new_ab()
b9.pitch_list("c c s")
b9.out("K")

# 6. HOU #29 Brett Wallace (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b c f f f f")
b9.hit(1)

# 7. HOU #30 Matt Dominguez (X - X - 29)
b9.new_ab()
b9.pitch_list("c f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #36 Junichi Tazawa
game.winning_pitcher(36, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: HOU
# LP: HOU #35 Josh Fields
game.losing_pitcher(35)

# print(game)
game.generate_scorecard()
