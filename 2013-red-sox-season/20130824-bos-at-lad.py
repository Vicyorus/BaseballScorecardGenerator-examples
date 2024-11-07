import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAD, 2013-08-24
# https://www.baseball-reference.com/boxes/LAN/LAN201308240.shtml
# https://www.mlb.com/gameday/red-sox-vs-dodgers/2013/08/24/348666/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-24 16:07-19:21",
        "at": "Dodger Stadium, Los Angeles, CA",
        "att": "48,165",
        "temp": "82F, Sunny",
        "wind": "7mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                3: "David Ross",
                31: "Jon Lester",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                34: "David Ortiz",
                29: "Daniel Nava",
                72: "Xander Bogaerts",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                60: "Brayan Villarreal",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 32, 66, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [5, "7"],
                [7, "6"],
                [16, "5"],
                [3, "2"],
                [31, "1"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [34, "DH"],
                [29, "LF"],
                [72, "2B"],
            ],
            "bullpen": [41, 67, 56, 60, 32, 66, 44, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Los Angeles Dodgers",
            "starter": 99,
            "roster": {
                # Lineup
                66: "Yasiel Puig",
                14: "Mark Ellis",
                23: "Adrián González",
                13: "Hanley Ramirez",
                17: "A.J. Ellis",
                16: "Andre Ethier",
                5: "Juan Uribe",
                6: "Jerry Hairston",
                99: "Hyun Jin Ryu",
                # Starting pitcher
                99: "Hyun Jin Ryu",
                # Bench
                25: "Carl Crawford",
                18: "Tim Federowicz",
                7: "Nick Punto",
                55: "Skip Schumaker",
                # Bullpen
                35: "Chris Capuano",
                21: "Zack Greinke",
                43: "Brandon League",
                75: "Paco Rodríguez",
                56: "J.P. Howell",
                74: "Kenley Jansen",
                22: "Clayton Kershaw",
                44: "Chris Withrow",
                49: "Carlos Marmol",
                0: "Brian Wilson",
                54: "Ronald Belisario",
                47: "Ricky Nolasco",
            },
            "lefties": [99, 35, 75, 56, 22],
            "lineup": [
                [66, "9"],
                [14, "4"],
                [23, "3"],
                [13, "6"],
                [17, "2"],
                [16, "8"],
                [5, "5"],
                [6, "7"],
                [99, "1"],
            ],
            "bench": [
                [25, "LF"],
                [18, "C"],
                [7, "2B"],
                [55, "2B"],
            ],
            "bullpen": [35, 21, 43, 75, 56, 74, 22, 44, 49, 0, 54, 47],
        },
        "umpires": {
            "HP": "Dan Iassogna",
            "1B": "Brian Knight",
            "2B": "Mark Carlson",
            "3B": "Gerry Davis",
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
# Pitching: LAD #99 Hyun Jin Ryu
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b f")
t1.reach("HBP")
t1.advance(2, "15 1B")
t1.advance(4, "12 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("c b 1 t f f b")
t1.hit(1)
t1.advance(2, "12 1B")
t1.advance(4, "5 HR")

# 4. BOS #12 Mike Napoli (X - 18 - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("c b")
t1.hit(1, rbis=1)
t1.advance(4, "5 HR")

# 5. BOS #5  Jonny Gomes (X - 15 - 12)
t1.new_ab(is_risp=True)
t1.hit(4, rbis=3)

# 6. BOS #7  Stephen Drew (X - X - X)
t1.new_ab()
t1.pitch_list("b c f f b c")
t1.out("!K")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t1.new_ab()
t1.pitch_list("b s b b s s")
t1.out("K")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. LAD #66 Yasiel Puig (X - X - X)
b1.new_ab()
b1.pitch_list("s b b b c f b")
b1.reach("BB")
b1.thrown_out(1, "23 DP3", 3, 31)

# 2. LAD #14 Mark Ellis (X - X - 66)
b1.new_ab()
b1.pitch_list("b c f f s")
b1.out("K")

# 3. LAD #23 Adrián González (X - X - 66)
b1.new_ab()
b1.pitch_list("c")
b1.out("DP3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAD #99 Hyun Jin Ryu
t2 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G5-3")

# 9. BOS #31 Jon Lester (X - X - X)
t2.new_ab()
t2.pitch_list("c c s")
t2.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t2.new_ab()
t2.pitch_list("b s")
t2.out("L7")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 4. LAD #13 Hanley Ramirez (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.out("P5")

# 5. LAD #17 A.J. Ellis (X - X - X)
b2.new_ab()
b2.pitch_list("c f c")
b2.out("!K")

# 6. LAD #16 Andre Ethier (X - X - X)
b2.new_ab()
b2.pitch_list("f")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAD #99 Hyun Jin Ryu
t3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c l")
t3.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F8")

# 4. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f b")
t3.hit(1)

# 5. BOS #5  Jonny Gomes (X - X - 12)
t3.new_ab()
t3.pitch_list("f b c b f b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 7. LAD #5  Juan Uribe (X - X - X)
b3.new_ab()
b3.out("F7")

# 8. LAD #6  Jerry Hairston (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.error(3)
b3.reach("E3")
b3.advance(2, "99 SAC3")

# 9. LAD #99 Hyun Jin Ryu (X - X - 6)
b3.new_ab()
b3.out("SAC3")

# 1. LAD #66 Yasiel Puig (X - 6 - X)
b3.new_ab(is_risp=True)
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAD #99 Hyun Jin Ryu
t4 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.hit(2)

# 7. BOS #16 Will Middlebrooks (X - 7 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c c b f f b")
t4.out("G5-3")

# 8. BOS #3  David Ross (X - 7 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("f c b t")
t4.out("KT")

# 9. BOS #31 Jon Lester (X - 7 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c c s")
t4.out("K")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 2. LAD #14 Mark Ellis (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.advance(2, "17 BB")

# 3. LAD #23 Adrián González (X - X - 14)
b4.new_ab()
b4.pitch_list("b b c f c")
b4.out("!K")

# 4. LAD #13 Hanley Ramirez (X - X - 14)
b4.new_ab()
b4.pitch_list("s f f c")
b4.out("!K")

# 5. LAD #17 A.J. Ellis (X - X - 14)
b4.new_ab()
b4.pitch_list("f b b b c f b")
b4.reach("BB")

# 6. LAD #16 Andre Ethier (X - 14 - 17)
b4.new_ab(is_risp=True)
b4.pitch_list("b")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAD #99 Hyun Jin Ryu
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("f b s b")
t5.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c f f t")
t5.out("KT")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b s b")
t5.out("L6")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 7. LAD #5  Juan Uribe (X - X - X)
b5.new_ab()
b5.pitch_list("c c b b f s")
b5.out("K2-3")

# 8. LAD #6  Jerry Hairston (X - X - X)
b5.new_ab()
b5.pitch_list("f f b f b f")
b5.out("F9")

# Offensive change (LAD): Pinch-hitter #7 Nick Punto replaces #99 Hyun Jin Ryu, batting 9th
b5.offensive_substitution(9, 7, "PH")

# 9. LAD #7  Nick Punto (X - X - X)
b5.new_ab()
b5.pitch_list("c b b f")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAD #49 Carlos Marmol
t6 = game.new_inning()

# Pitching change (LAD): #49 Carlos Marmol replaces #99 Hyun Jin Ryu, batting 9th
t6.pitching_substitution(49)
t6.defensive_substitution(9, 49, "1")

# 4. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("b c c b f s")
t6.out("K")

# 5. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("b b c b c b")
t6.reach("BB")
t6.advance(2, "16 SB")

# 6. BOS #7  Stephen Drew (X - X - 5)
t6.new_ab()
t6.pitch_list("1 1 c c 1 b s")
t6.out("K")

# 7. BOS #16 Will Middlebrooks (X - X - 5)
t6.new_ab(is_risp=True)
t6.pitch_list("1 c 1 t b s")
t6.out("K")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 1. LAD #66 Yasiel Puig (X - X - X)
b6.new_ab()
b6.pitch_list("s b f")
b6.hit(1)
b6.thrown_out(1, "14 DP9-3", 2, 31)

# 2. LAD #14 Mark Ellis (X - X - 66)
b6.new_ab()
b6.pitch_list("c b")
b6.out("DP9-3")

# 3. LAD #23 Adrián González (X - X - X)
b6.new_ab()
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAD #49 Carlos Marmol
t7 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("P4")

# Pitching change (LAD): #56 J.P. Howell replaces #49 Carlos Marmol, batting 9th
t7.pitching_substitution(56)
t7.defensive_substitution(9, 56, "1")

# 9. BOS #31 Jon Lester (X - X - X)
t7.new_ab()
t7.pitch_list("c f b f c")
t7.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("c b c b b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 4. LAD #13 Hanley Ramirez (X - X - X)
b7.new_ab()
b7.pitch_list("b f b b b")
b7.reach("BB")
b7.advance(2, "16 1B")
b7.thrown_out(2, "5 DP6", 3, 31)

# 5. LAD #17 A.J. Ellis (X - X - 13)
b7.new_ab()
b7.pitch_list("b c b f f s")
b7.out("K")

# 6. LAD #16 Andre Ethier (X - X - 13)
b7.new_ab()
b7.pitch_list("b s")
b7.hit(1)

# 7. LAD #5  Juan Uribe (X - 13 - 16)
b7.new_ab(is_risp=True)
b7.pitch_list("b c")
b7.out("DP6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAD #0  Brian Wilson
t8 = game.new_inning()

# Pitching change (LAD): #0  Brian Wilson replaces #56 J.P. Howell, batting 9th
t8.pitching_substitution(0)
t8.defensive_substitution(9, 0, "1")

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b")
t8.hit(2)
t8.advance(3, "12 1B")

# 4. BOS #12 Mike Napoli (X - 15 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b b c")
t8.hit(1)
t8.advance(2, "7 BB")

# 5. BOS #5  Jonny Gomes (15 - X - 12)
t8.new_ab(is_risp=True)
t8.pitch_list("b c")
t8.out("P4")

# 6. BOS #7  Stephen Drew (15 - X - 12)
t8.new_ab(is_risp=True)
t8.pitch_list("b f b c b f b")
t8.reach("BB")

# 7. BOS #16 Will Middlebrooks (15 - 12 - 7)
t8.new_ab(is_risp=True)
t8.pitch_list("f b f b c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #31 Jon Lester
b8 = game.new_inning()

# 8. LAD #6  Jerry Hairston (X - X - X)
b8.new_ab()
b8.pitch_list("b f f b")
b8.out("P6")

# Offensive change (LAD): Pinch-hitter #25 Carl Crawford replaces #0 Brian Wilson, batting 9th
b8.offensive_substitution(9, 25, "PH")

# 9. LAD #25 Carl Crawford (X - X - X)
b8.new_ab()
b8.pitch_list("b f b s b b")
b8.reach("BB")
b8.advance(2, "66 1B")
b8.advance(4, "23 2B")

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester, batting 9th
b8.pitching_substitution(36)
b8.defensive_substitution(9, 36, "1")

# 1. LAD #66 Yasiel Puig (X - X - 25)
b8.new_ab()
b8.pitch_list("c b b f")
b8.hit(1)
b8.advance(4, "23 2B")

# 2. LAD #14 Mark Ellis (X - 25 - 66)
b8.new_ab(is_risp=True)
b8.pitch_list("c c b f t")
b8.out("KT")

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa, batting 9th
b8.pitching_substitution(32)
b8.defensive_substitution(9, 32, "1")

# 3. LAD #23 Adrián González (X - 25 - 66)
b8.new_ab(is_risp=True)
b8.pitch_list("b")
b8.hit(2, rbis=2)

# 4. LAD #13 Hanley Ramirez (X - 23 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b s b s d b")
b8.reach("BB")

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow, batting 7th
b8.pitching_substitution(19)
b8.defensive_substitution(7, 19, "1")

# Defensive change (BOS): #72 Xander Bogaerts replaces #32 Craig Breslow (P), playing 3B, batting 9th
b8.defensive_substitution(9, 72, "5")

# 5. LAD #17 A.J. Ellis (X - 23 - 13)
b8.new_ab(is_risp=True)
b8.pitch_list("s c b f b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAD #43 Brandon League
t9 = game.new_inning()

# Pitching change (LAD): #43 Brandon League replaces #0  Brian Wilson, batting 2nd
t9.pitching_substitution(43)
t9.defensive_substitution(2, 43, "1")

# Defensive switch (LAD): #6 Jerry Hairston moves to 2B
t9.defensive_switch(6, "4")

# Defensive switch (LAD): #25 Carl Crawford moves to LF
t9.defensive_switch(25, "7")

# 8. BOS #3  David Ross (X - X - X)
t9.new_ab()
t9.pitch_list("c s b b b")
t9.out("G6-3")

# 9. BOS #72 Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("b f b s")
t9.hit(1)
t9.thrown_out(2, "2 DP3-6", 2, 75)

# Pitching change (LAD): #75 Paco Rodríguez replaces #43 Brandon League, batting 2nd
t9.pitching_substitution(75)
t9.defensive_substitution(2, 75, "1")

# 1. BOS #2  Jacoby Ellsbury (X - X - 72)
t9.new_ab()
t9.pitch_list("1 c")
t9.out("DP3-6")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# 6. LAD #16 Andre Ethier (X - X - X)
b9.new_ab()
b9.pitch_list("c f")
b9.out("G4-3")

# 7. LAD #5  Juan Uribe (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("P5")

# 8. LAD #6  Jerry Hairston (X - X - X)
b9.new_ab()
b9.pitch_list("c s f")
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: LAD
# LP: LAD #99 Hyun Jin Ryu
game.losing_pitcher(99)

# print(game)
game.generate_scorecard()
