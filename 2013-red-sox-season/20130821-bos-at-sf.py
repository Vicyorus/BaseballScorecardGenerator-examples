import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ SF, 2013-08-21
# https://www.baseball-reference.com/boxes/SFN/SFN201308210.shtml
# https://www.mlb.com/gameday/red-sox-vs-giants/2013/08/21/348627/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-21 15:45-18:31",
        "at": "AT&T Park, San Francisco, CA",
        "att": "41,532",
        "temp": "68F, Overcast",
        "wind": "13mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                22: "Felix Doubront",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                29: "Daniel Nava",
                3: "David Ross",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                60: "Brayan Villarreal",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 32, 66, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
                [22, "1"],
            ],
            "bench": [
                [37, "1B"],
                [29, "LF"],
                [3, "C"],
                [72, "2B"],
                [12, "1B"],
            ],
            "bullpen": [41, 67, 56, 60, 32, 66, 44, 31, 36, 11, 19, 46],
        },
        "home": {
            "team": "San Francisco Giants",
            "starter": 75,
            "roster": {
                # Lineup
                56: "Andres Torres",
                19: "Marco Scutaro",
                9: "Brandon Belt",
                28: "Buster Posey",
                8: "Hunter Pence",
                13: "Joaquin Arias",
                22: "Roger Kieschnick",
                35: "Brandon Crawford",
                75: "Barry Zito",
                # Starting pitcher
                75: "Barry Zito",
                # Bench
                6: "Brett Pill",
                7: "Grégor Blanco",
                29: "Héctor Sánchez",
                48: "Pablo Sandoval",
                # Bullpen
                55: "Tim Lincecum",
                40: "Madison Bumgarner",
                63: "Jean Machi",
                43: "Sandy Rosario",
                34: "Guillermo Moscoso",
                32: "Ryan Vogelsong",
                50: "Jose Mijares",
                49: "Javier López",
                59: "Mike Kickham",
                18: "Matt Cain",
                46: "Santiago Casilla",
                54: "Sergio Romo",
            },
            "lefties": [75, 40, 50, 49, 59],
            "lineup": [
                [56, "8"],
                [19, "4"],
                [9, "3"],
                [28, "2"],
                [8, "9"],
                [13, "5"],
                [22, "7"],
                [35, "6"],
                [75, "1"],
            ],
            "bench": [
                [6, "1B"],
                [7, "CF"],
                [29, "C"],
                [48, "3B"],
            ],
            "bullpen": [55, 40, 63, 43, 34, 32, 50, 49, 59, 18, 46, 54],
        },
        "umpires": {
            "HP": "Dan Bellino",
            "1B": "Bruce Dreckman",
            "2B": "Tim Welke",
            "3B": "Mike Everitt",
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
# Pitching: SFG #75 Barry Zito
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(2)
t1.advance(3, "15 F9")

# 2. BOS #18 Shane Victorino (X - 2 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("m c f b f 2 s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b 2 b b")
t1.out("F9")

# 4. BOS #34 David Ortiz (2 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b d c b f")
t1.out("G3")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. SFG #56 Andres Torres (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.hit(1)
b1.thrown_out(2, "19 POCS", 1, 22)

# 2. SFG #19 Marco Scutaro (X - X - 56)
b1.new_ab()
b1.pitch_list("b b 1 b c c b")
b1.reach("BB")

# 3. SFG #9  Brandon Belt (X - X - 19)
b1.new_ab()
b1.pitch_list("f b b b")
b1.out("F9")

# 4. SFG #28 Buster Posey (X - X - 19)
b1.new_ab()
b1.pitch_list("b f f d")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SFG #75 Barry Zito
t2 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b f c")
t2.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c b")
t2.reach("BB")
t2.advance(4, "16 HR")

# 7. BOS #7  Stephen Drew (X - X - 39)
t2.new_ab()
t2.pitch_list("f b b f f b f f")
t2.out("F9")

# 8. BOS #16 Will Middlebrooks (X - X - 39)
t2.new_ab()
t2.pitch_list("c")
t2.hit(4, rbis=2)

# 9. BOS #22 Felix Doubront (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G5-3")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 5. SFG #8  Hunter Pence (X - X - X)
b2.new_ab()
b2.pitch_list("b b c c s")
b2.out("K")

# 6. SFG #13 Joaquin Arias (X - X - X)
b2.new_ab()
b2.pitch_list("c b s b b")
b2.hit(4)

# 7. SFG #22 Roger Kieschnick (X - X - X)
b2.new_ab()
b2.pitch_list("b f c b")
b2.out("G4-3")

# 8. SFG #35 Brandon Crawford (X - X - X)
b2.new_ab()
b2.pitch_list("b c b f b f f")
b2.out("P6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SFG #75 Barry Zito
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("s f b b b")
t3.hit(1)
t3.advance(2, "18 SB")
t3.advance(3, "18 1B")
t3.advance(4, "15 2B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.hit(1)
t3.advance(3, "15 2B")
t3.advance(4, "5 1B")

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
t3.new_ab(is_risp=True)
t3.pitch_list("c f 1 b b f 1")
t3.hit(2, rbis=1)
t3.advance(4, "5 1B")

# 4. BOS #34 David Ortiz (18 - 15 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b s t")
t3.out("KT")

# 5. BOS #5  Jonny Gomes (18 - 15 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f s b")
t3.hit(1, rbis=2)
t3.thrown_out(2, "39 FC6-4", 2, 75)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 5)
t3.new_ab()
t3.pitch_list("c")
t3.reach("FC6-4")

# 7. BOS #7  Stephen Drew (X - X - 39)
t3.new_ab()
t3.pitch_list("d b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 9. SFG #75 Barry Zito (X - X - X)
b3.new_ab()
b3.pitch_list("b c b s t")
b3.out("KT")

# 1. SFG #56 Andres Torres (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G6-3")

# 2. SFG #19 Marco Scutaro (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SFG #75 Barry Zito
t4 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c c b")
t4.reach("BB")
t4.advance(2, "22 SAC2-4")
t4.advance(4, "18 2B")

# 9. BOS #22 Felix Doubront (X - X - 16)
t4.new_ab()
t4.pitch_list("l b 1")
t4.out("SAC2-4")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
t4.new_ab(is_risp=True)
t4.out("F7")

# 2. BOS #18 Shane Victorino (X - 16 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b")
t4.hit(2, rbis=1)

# Pitching change (SFG): #63 Jean Machi replaces #75 Barry Zito, batting 9th
t4.pitching_substitution(63)
t4.defensive_substitution(9, 63, "1")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
t4.new_ab(is_risp=True)
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 3. SFG #9  Brandon Belt (X - X - X)
b4.new_ab()
b4.pitch_list("b b f")
b4.out("F7")

# 4. SFG #28 Buster Posey (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("F9")

# 5. SFG #8  Hunter Pence (X - X - X)
b4.new_ab()
b4.pitch_list("f c b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SFG #63 Jean Machi
t5 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("c c b s")
t5.out("K")

# 5. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("c c s")
t5.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("c b c f b b")
t5.out("F8")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# Defensive change (BOS): #12 Mike Napoli replaces #34 David Ortiz (1B), playing 1B, batting 4th
b5.defensive_substitution(4, 12, "3")

# 6. SFG #13 Joaquin Arias (X - X - X)
b5.new_ab()
b5.hit(1)

# 7. SFG #22 Roger Kieschnick (X - X - 13)
b5.new_ab()
b5.pitch_list("c f b b f b")
b5.out("P4")

# 8. SFG #35 Brandon Crawford (X - X - 13)
b5.new_ab()
b5.pitch_list("c d f")
b5.out("L7")

# Offensive change (SFG): Pinch-hitter #6 Brett Pill replaces #63 Jean Machi, batting 9th
b5.offensive_substitution(9, 6, "PH")

# 9. SFG #6  Brett Pill (X - X - 13)
b5.new_ab()
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SFG #59 Mike Kickham
t6 = game.new_inning()

# Pitching change (SFG): #59 Mike Kickham replaces #63 Jean Machi, batting 9th
t6.pitching_substitution(59)
t6.defensive_substitution(9, 59, "1")

# 7. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.out("G3")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t6.new_ab()
t6.pitch_list("b c s b b")
t6.out("G6-3")

# 9. BOS #22 Felix Doubront (X - X - X)
t6.new_ab()
t6.pitch_list("c c b b s")
t6.out("K")


# Bot 6th
# Pitching: BOS #22 Felix Doubront
b6 = game.new_inning()

# 1. SFG #56 Andres Torres (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b f b")
b6.out("P6")

# 2. SFG #19 Marco Scutaro (X - X - X)
b6.new_ab()
b6.out("F8")

# 3. SFG #9  Brandon Belt (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SFG #59 Mike Kickham
t7 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(3, "15 2B")
t7.advance(4, "39 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t7.new_ab()
t7.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t7.new_ab()
t7.pitch_list("c s b")
t7.hit(2)
t7.advance(4, "39 1B")

# 4. BOS #12 Mike Napoli (2 - 15 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c f f s")
t7.out("K")

# 5. BOS #5  Jonny Gomes (2 - 15 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c b b b b")
t7.reach("BB")
t7.advance(2, "39 1B")
t7.advance(4, "7 HR")

# 6. BOS #39 Jarrod Saltalamacchia (2 - 15 - 5)
t7.new_ab(is_risp=True)
t7.pitch_list("c")
t7.hit(1, rbis=2)
t7.advance(4, "7 HR")

# 7. BOS #7  Stephen Drew (X - 5 - 39)
t7.new_ab(is_risp=True)
t7.pitch_list("c b d")
t7.hit(4, rbis=3)

# 8. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #22 Felix Doubront
b7 = game.new_inning()

# Defensive change (BOS): #72 Xander Bogaerts replaces #15 Dustin Pedroia (2B), playing 3B, batting 3rd
b7.defensive_substitution(3, 72, "5")

# Defensive switch (BOS): #16 Will Middlebrooks moves to 2B
b7.defensive_switch(16, "4")

# 4. SFG #28 Buster Posey (X - X - X)
b7.new_ab()
b7.hit(1)
b7.thrown_out(2, "8 DP6-4-3", 1, 22)

# 5. SFG #8  Hunter Pence (X - X - 28)
b7.new_ab()
b7.pitch_list("d b")
b7.out("DP6-4-3")

# 6. SFG #13 Joaquin Arias (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SFG #59 Mike Kickham
t8 = game.new_inning()

# Defensive change (SFG): #29 Héctor Sánchez replaces #28 Buster Posey (C), playing C, batting 4th
t8.defensive_substitution(4, 29, "2")

# 9. BOS #22 Felix Doubront (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("G1-3")

# Offensive change (BOS): Pinch-hitter #29 Daniel Nava replaces #2 Jacoby Ellsbury, batting 1st
t8.offensive_substitution(1, 29, "PH")

# 1. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.error(4)
t8.reach("E4")
t8.advance(2, "18 1B")
t8.error(1)
t8.advance(3, "72 FC1")
t8.advance("U", "72 E1")

# 2. BOS #18 Shane Victorino (X - X - 29)
t8.new_ab()
t8.pitch_list("b b b c c")
t8.hit(1)
t8.advance(3, "72 E1")

# 3. BOS #72 Xander Bogaerts (X - 29 - 18)
t8.new_ab(is_risp=True)
t8.pitch_list("d b")
t8.reach("FC1")
t8.thrown_out(2, "12 DP5-4-3", 2, 59)

# 4. BOS #12 Mike Napoli (18 - X - 72)
t8.new_ab(is_risp=True)
t8.pitch_list("s")
t8.out("DP5-4-3")


# Bot 8th
# Pitching: BOS #22 Felix Doubront
b8 = game.new_inning()

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b8.defensive_switch(29, "9")

# Defensive switch (BOS): #18 Shane Victorino moves to CF
b8.defensive_switch(18, "8")

# 7. SFG #22 Roger Kieschnick (X - X - X)
b8.new_ab()
b8.pitch_list("b b s f")
b8.out("G3")

# 8. SFG #35 Brandon Crawford (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.thrown_out(2, "6 FC1-6", 2, 22)

# 9. SFG #6  Brett Pill (X - X - 35)
b8.new_ab()
b8.pitch_list("b s f")
b8.reach("FC1-6")

# 1. SFG #56 Andres Torres (X - X - 59)
b8.new_ab()
b8.pitch_list("b f b b f f f f")
b8.out("(F)F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SFG #59 Mike Kickham
t9 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("b c b c s")
t9.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("s b c")
t9.out("G1-3")

# 7. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c f b f b")
t9.out("F7")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #22 Felix Doubront, batting 9th
b9.pitching_substitution(19)
b9.defensive_substitution(9, 19, "1")

# 2. SFG #19 Marco Scutaro (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G4-3")

# 3. SFG #9  Brandon Belt (X - X - X)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# 4. SFG #29 Héctor Sánchez (X - X - X)
b9.new_ab()
b9.out("G6-3")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22, is_away_team=True)

# Loser team: SFG
# LP: SFG #75 Barry Zito
game.losing_pitcher(75)

# print(game)
game.generate_scorecard()
