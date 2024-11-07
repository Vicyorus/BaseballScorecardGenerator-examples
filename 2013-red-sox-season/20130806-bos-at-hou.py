import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ HOU, 2013-08-06
# https://www.baseball-reference.com/boxes/HOU/HOU201308060.shtml
# https://www.mlb.com/gameday/red-sox-vs-astros/2013/08/06/348423/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-06 20:11-00:05 +1",
        "at": "Minute Maid Park, Houston, TX",
        "att": "21,615",
        "temp": "73F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 35,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                7: "Stephen Drew",
                20: "Ryan Lavarnway",
                26: "Brock Holt",
                # Starting pitcher
                35: "Steven Wright",
                # Bench
                39: "Jarrod Saltalamacchia",
                5: "Jonny Gomes",
                23: "Brandon Snyder",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                19: "Koji Uehara",
                66: "Drake Britton",
                44: "Jake Peavy",
                62: "Rubby De La Rosa",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [7, "6"],
                [20, "2"],
                [26, "5"],
            ],
            "bench": [
                [39, "C"],
                [5, "LF"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 32, 19, 66, 44, 62, 31, 36, 22, 46],
        },
        "home": {
            "team": "Houston Astros",
            "starter": 18,
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
                6: "Jonathan Villar",
                # Starting pitcher
                18: "Jordan Lyles",
                # Bench
                23: "Chris Carter",
                10: "Jake Elmore",
                22: "Carlos Corporán",
                # Bullpen
                45: "Erik Bedard",
                53: "Wesley Wright",
                39: "Brett Oberholtzer",
                63: "Chia-Jen Lo",
                64: "Lucas Harrell",
                35: "Josh Fields",
                54: "Travis Blackley",
                60: "Dallas Keuchel",
                48: "Jarred Cosart",
                41: "Brad Peacock",
                68: "José Cisnero",
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
                [6, "6"],
            ],
            "bench": [
                [23, "1B"],
                [10, "2B"],
                [22, "C"],
            ],
            "bullpen": [45, 53, 39, 63, 64, 35, 54, 60, 48, 41, 68, 61],
        },
        "umpires": {
            "HP": "Brian Knight",
            "1B": "Mark Carlson",
            "2B": "Gerry Davis",
            "3B": "Dan Iassogna",
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
# Pitching: HOU #18 Jordan Lyles
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.out("L6")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c f")
t1.out("G3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c f f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #35 Steven Wright
b1 = game.new_inning()

# 1. HOU #19 Robbie Grossman (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c c b")
b1.reach("BB")
b1.advance(2, "2 SB")
b1.advance(3, "2 PB")
b1.advance(4, "27 PB")

# 2. HOU #2  Brandon Barnes (X - X - 19)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b")
b1.pb()
b1.reach("HBP")
b1.advance(2, "27 PB")
b1.advance(3, "27 PB")
b1.advance(4, "15 PB")

# 3. HOU #27 Jose Altuve (19 - X - 2)
b1.new_ab(is_risp=True)
b1.pitch_list("1 b s f b d s")
b1.pb()
b1.pb()
b1.out("K")

# 4. HOU #15 Jason Castro (2 - X - X)
b1.new_ab()
b1.pitch_list("b c f b f b")
b1.pb()
b1.hit(1)
b1.advance(2, "59 BB")
b1.advance(3, "29 WP")
b1.advance(4, "29 G4-3")

# 5. HOU #59 Marc Krauss (X - X - 15)
b1.new_ab()
b1.pitch_list("b s b s f b f f b")
b1.reach("BB")
b1.advance(2, "29 WP")
b1.advance(3, "29 G4-3")

# 6. HOU #29 Brett Wallace (X - 15 - 59)
b1.new_ab(is_risp=True)
b1.pitch_list("b b f")
b1.wp()
b1.out("G4-3", rbis=1)

# 7. HOU #30 Matt Dominguez (59 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: HOU #18 Jordan Lyles
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c b b f b")
t2.hit(1)
t2.thrown_out(2, "12 DP6-4-3", 1, 18)

# 5. BOS #12 Mike Napoli (X - X - 34)
t2.new_ab()
t2.pitch_list("s b")
t2.out("DP6-4-3")

# 6. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("b c f t")
t2.out("KT")


# Bot 2nd
# Pitching: BOS #67 Brandon Workman
b2 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #35 Steven Wright
b2.pitching_substitution(67)

# 8. HOU #28 L.J. Hoes (X - X - X)
b2.new_ab()
b2.pitch_list("c b f f b f b s")
b2.out("K")

# 9. HOU #6  Jonathan Villar (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.hit(1)
b2.advance(2, "19 SB")
b2.advance(4, "19 HR")

# 1. HOU #19 Robbie Grossman (X - X - 6)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c b")
b2.hit(4, rbis=2)

# 2. HOU #2  Brandon Barnes (X - X - X)
b2.new_ab()
b2.pitch_list("c s f")
b2.out("G6-3")

# 3. HOU #27 Jose Altuve (X - X - X)
b2.new_ab()
b2.out("(F)F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: HOU #18 Jordan Lyles
t3 = game.new_inning()

# 7. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.hit(1)
t3.thrown_out(2, "26 FC5-4", 2, 18)

# 8. BOS #20 Ryan Lavarnway (X - X - 7)
t3.new_ab()
t3.pitch_list("c b b t c")
t3.out("!K")

# 9. BOS #26 Brock Holt (X - X - 7)
t3.new_ab()
t3.pitch_list("c")
t3.reach("FC5-4")
t3.advance(4, "2 HR")

# 1. BOS #2  Jacoby Ellsbury (X - X - 26)
t3.new_ab()
t3.pitch_list("c b b b")
t3.hit(4, rbis=2)

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c s")
t3.hit(1)
t3.advance(2, "15 HBP")
t3.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t3.new_ab()
t3.pitch_list("1 c b c")
t3.reach("HBP")
t3.advance(3, "34 1B")

# 4. BOS #34 David Ortiz (X - 18 - 15)
t3.new_ab(is_risp=True)
t3.pitch_list("b c d")
t3.hit(1, rbis=1)

# 5. BOS #12 Mike Napoli (15 - X - 34)
t3.new_ab(is_risp=True)
t3.pitch_list("s c s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #67 Brandon Workman
b3 = game.new_inning()

# 4. HOU #15 Jason Castro (X - X - X)
b3.new_ab()
b3.pitch_list("c c f b b s")
b3.out("K")

# 5. HOU #59 Marc Krauss (X - X - X)
b3.new_ab()
b3.pitch_list("b c b")
b3.out("F7")

# 6. HOU #29 Brett Wallace (X - X - X)
b3.new_ab()
b3.pitch_list("b c b")
b3.hit(4)

# 7. HOU #30 Matt Dominguez (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: HOU #18 Jordan Lyles
t4 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G4-3")

# 7. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("b s b b b")
t4.reach("BB")

# 8. BOS #20 Ryan Lavarnway (X - X - 7)
t4.new_ab()
t4.pitch_list("f b c s")
t4.out("K")

# 9. BOS #26 Brock Holt (X - X - 7)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G1-3")


# Bot 4th
# Pitching: BOS #67 Brandon Workman
b4 = game.new_inning()

# 8. HOU #28 L.J. Hoes (X - X - X)
b4.new_ab()
b4.hit(3)
b4.advance(4, "6 1B")

# 9. HOU #6  Jonathan Villar (28 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c b d b")
b4.hit(1, rbis=1)
b4.advance(2, "19 SAC5-3")
b4.thrown_out(3, "27 CS", 2, 67)

# 1. HOU #19 Robbie Grossman (X - X - 6)
b4.new_ab()
b4.out("SAC5-3")

# 2. HOU #2  Brandon Barnes (X - 6 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("s b b f b b")
b4.reach("BB")
b4.advance(2, "27 CS")

# 3. HOU #27 Jose Altuve (X - 6 - 2)
b4.new_ab(is_risp=True)
b4.pitch_list("c b b b f")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: HOU #18 Jordan Lyles
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("b b c b b")
t5.reach("BB")
t5.error(9)
t5.advance(3, "18 2B")
t5.advance(4, "18 E9")

# 2. BOS #18 Shane Victorino (X - X - 2)
t5.new_ab()
t5.pitch_list("c")
t5.hit(2)
t5.advance(4, "15 2B")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c b")
t5.hit(2, rbis=1)
t5.advance(3, "34 1B")
t5.advance(4, "37 G3")

# 4. BOS #34 David Ortiz (X - 15 - X)
t5.new_ab(is_risp=True)
t5.hit(1)
t5.advance(2, "37 G3")
t5.advance(3, "7 WP")
t5.advance(4, "20 2B")

# 5. BOS #12 Mike Napoli (15 - X - 34)
t5.new_ab(is_risp=True)
t5.pitch_list("c f d t")
t5.out("KT")

# 6. BOS #37 Mike Carp (15 - X - 34)
t5.new_ab(is_risp=True)
t5.out("G3", rbis=1)

# 7. BOS #7  Stephen Drew (X - 34 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c c d b")
t5.wp()
t5.reach("BB")
t5.advance(4, "20 2B")

# 8. BOS #20 Ryan Lavarnway (34 - X - 7)
t5.new_ab(is_risp=True)
t5.hit(2, rbis=2)

# Pitching change (HOU): #60 Dallas Keuchel replaces #18 Jordan Lyles
t5.pitching_substitution(60)

# 9. BOS #26 Brock Holt (X - 20 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("s")
t5.out("G5-3")


# Bot 5th
# Pitching: BOS #67 Brandon Workman
b5 = game.new_inning()

# 4. HOU #15 Jason Castro (X - X - X)
b5.new_ab()
b5.pitch_list("f c f b b b b")
b5.reach("BB")
b5.thrown_out(2, "29 DP3-6-3", 2, 67)

# 5. HOU #59 Marc Krauss (X - X - 15)
b5.new_ab()
b5.out("F9")

# 6. HOU #29 Brett Wallace (X - X - 15)
b5.new_ab()
b5.pitch_list("c 1 b b")
b5.out("DP3-6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: HOU #60 Dallas Keuchel
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("f b s b f b f b")
t6.reach("BB")
t6.advance(2, "18 1B")
t6.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t6.new_ab()
t6.hit(1)
t6.advance(2, "15 1B")
t6.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t6.new_ab(is_risp=True)
t6.pitch_list("c b d")
t6.hit(1, rbis=1)
t6.error(6)
t6.advance(2, "34 1B")
t6.advance(3, "34 E6")
t6.thrown_out(4, "12 FC4", 1, 60)

# 4. BOS #34 David Ortiz (X - 18 - 15)
t6.new_ab(is_risp=True)
t6.pitch_list("f s")
t6.hit(1, rbis=1)
t6.advance(2, "E6")
t6.advance(3, "12 FC4")
t6.advance(4, "5 HR")

# Defensive change (HOU): #10 Jake Elmore replaces #6 Jonathan Villar (SS), playing SS, batting 9th
t6.defensive_substitution(9, 10, "6")

# 5. BOS #12 Mike Napoli (15 - 34 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b s f b f")
t6.reach("FC4", end_base=2)
t6.advance(4, "5 HR")

# Pitching change (HOU): #68 José Cisnero replaces #60 Dallas Keuchel
t6.pitching_substitution(68)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 6th
t6.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Jonny Gomes (34 - 12 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("d")
t6.hit(4, rbis=3)

# 7. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b b")
t6.reach("BB")

# 8. BOS #20 Ryan Lavarnway (X - X - 7)
t6.new_ab()
t6.pitch_list("f")
t6.out("F8")

# 9. BOS #26 Brock Holt (X - X - 7)
t6.new_ab()
t6.pitch_list("c f b f")
t6.out("F7")


# Bot 6th
# Pitching: BOS #67 Brandon Workman
b6 = game.new_inning()

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b6.defensive_switch(5, "7")

# 7. HOU #30 Matt Dominguez (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G6-3")

# 8. HOU #28 L.J. Hoes (X - X - X)
b6.new_ab()
b6.pitch_list("c c b f b f b")
b6.hit(1)
b6.advance(2, "10 1B")
b6.advance(4, "19 1B")

# 9. HOU #10 Jake Elmore (X - X - 28)
b6.new_ab()
b6.pitch_list("b b c")
b6.hit(1)
b6.advance(2, "19 1B")
b6.advance(3, "2 1B")
b6.advance(4, "27 G4-3")

# 1. HOU #19 Robbie Grossman (X - 28 - 10)
b6.new_ab(is_risp=True)
b6.pitch_list("b c")
b6.hit(1, rbis=1)
b6.advance(2, "2 1B")
b6.advance(3, "27 G4-3")

# 2. HOU #2  Brandon Barnes (X - 10 - 19)
b6.new_ab(is_risp=True)
b6.pitch_list("d")
b6.hit(1)
b6.advance(2, "27 G4-3")

# 3. HOU #27 Jose Altuve (10 - 19 - 2)
b6.new_ab(is_risp=True)
b6.pitch_list("c")
b6.out("G4-3", rbis=1)

# Pitching change (BOS): #66 Drake Britton replaces #67 Brandon Workman
b6.pitching_substitution(66)

# 4. HOU #15 Jason Castro (19 - 2 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c c b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: HOU #68 José Cisnero
t7 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("c b b")
t7.hit(4)

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")
t7.advance(2, "34 BLK")
t7.advance(3, "12 BB")
t7.advance(4, "5 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t7.new_ab()
t7.pitch_list("c b")
t7.out("P4")

# 4. BOS #34 David Ortiz (X - X - 18)
t7.new_ab(is_risp=True)
t7.pitch_list("c b b b n b")
t7.balk()
t7.reach("BB")
t7.advance(2, "12 BB")
t7.advance(3, "5 1B")
t7.thrown_out(4, "7 FC5-2", 2, 61)

# Pitching change (HOU): #61 Josh Zeid replaces #68 José Cisnero
t7.pitching_substitution(61)

# 5. BOS #12 Mike Napoli (X - 18 - 34)
t7.new_ab(is_risp=True)
t7.pitch_list("c b f b b b")
t7.reach("BB")
t7.advance(2, "5 1B")
t7.advance(3, "7 FC5-2")

# 6. BOS #5  Jonny Gomes (18 - 34 - 12)
t7.new_ab(is_risp=True)
t7.hit(1, rbis=1)
t7.advance(2, "7 FC5-2")

# 7. BOS #7  Stephen Drew (34 - 12 - 5)
t7.new_ab(is_risp=True)
t7.pitch_list("c s")
t7.reach("FC5-2")

# 8. BOS #20 Ryan Lavarnway (12 - 5 - 7)
t7.new_ab(is_risp=True)
t7.pitch_list("c b s s")
t7.out("K")


# Bot 7th
# Pitching: BOS #66 Drake Britton
b7 = game.new_inning()

# 5. HOU #59 Marc Krauss (X - X - X)
b7.new_ab()
b7.pitch_list("b c b s b")
b7.out("G4-3")

# 6. HOU #29 Brett Wallace (X - X - X)
b7.new_ab()
b7.pitch_list("c f f f b s")
b7.out("K")

# 7. HOU #30 Matt Dominguez (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: HOU #61 Josh Zeid
t8 = game.new_inning()

# Defensive change (HOU): #22 Carlos Corporán replaces #15 Jason Castro (C), playing C, batting 4th
t8.defensive_substitution(4, 22, "2")

# 9. BOS #26 Brock Holt (X - X - X)
t8.new_ab()
t8.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("b c b b c t")
t8.out("KT")

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("b b c f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #66 Drake Britton
b8 = game.new_inning()

# 8. HOU #28 L.J. Hoes (X - X - X)
b8.new_ab()
b8.pitch_list("c s b s")
b8.out("K")

# 9. HOU #10 Jake Elmore (X - X - X)
b8.new_ab()
b8.pitch_list("b s b")
b8.hit(4)

# 1. HOU #19 Robbie Grossman (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("L9")

# 2. HOU #2  Brandon Barnes (X - X - X)
b8.new_ab()
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: HOU #63 Chia-Jen Lo
t9 = game.new_inning()

# Pitching change (HOU): #63 Chia-Jen Lo replaces #61 Josh Zeid
t9.pitching_substitution(63)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("f b")
t9.out("P6")

# Offensive change (BOS): Pinch-hitter #23 Brandon Snyder replaces #34 David Ortiz, batting 4th
t9.offensive_substitution(4, 23, "PH")

# 4. BOS #23 Brandon Snyder (X - X - X)
t9.new_ab()
t9.pitch_list("s b")
t9.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b c c b b b")
t9.reach("BB")

# 6. BOS #5  Jonny Gomes (X - X - 12)
t9.new_ab()
t9.pitch_list("c c c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #62 Rubby De La Rosa
b9 = game.new_inning()

# Pitching change (BOS): #62 Rubby De La Rosa replaces #66 Drake Britton
b9.pitching_substitution(62)

# Defensive switch (BOS): #23 Brandon Snyder moves to DH
b9.defensive_switch(23, "0")

# 3. HOU #27 Jose Altuve (X - X - X)
b9.new_ab()
b9.pitch_list("b c c b")
b9.out("G2-3")

# 4. HOU #22 Carlos Corporán (X - X - X)
b9.new_ab()
b9.pitch_list("c f f s")
b9.out("K")

# 5. HOU #59 Marc Krauss (X - X - X)
b9.new_ab()
b9.pitch_list("s s b b f f t")
b9.out("KT")

# Winning team: BOS
# WP: BOS #67 Brandon Workman
game.winning_pitcher(67, is_away_team=True)

# Loser team: HOU
# LP: HOU #18 Jordan Lyles
game.losing_pitcher(18)

# print(game)
game.generate_scorecard()
