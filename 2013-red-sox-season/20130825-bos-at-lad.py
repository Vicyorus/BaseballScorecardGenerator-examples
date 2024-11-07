import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAD, 2013-08-25
# https://www.baseball-reference.com/boxes/LAN/LAN201308250.shtml
# https://www.mlb.com/gameday/red-sox-vs-dodgers/2013/08/25/348679/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-25 20:08-23:08",
        "at": "Dodger Stadium, Los Angeles, CA",
        "att": "44,109",
        "temp": "80F, Clear",
        "wind": "4mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                72: "Xander Bogaerts",
                44: "Jake Peavy",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                7: "Stephen Drew",
                37: "Mike Carp",
                34: "David Ortiz",
                29: "Daniel Nava",
                3: "David Ross",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                38: "Matt Thornton",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [5, "7"],
                [16, "5"],
                [39, "2"],
                [72, "6"],
                [44, "1"],
            ],
            "bench": [
                [7, "SS"],
                [37, "1B"],
                [34, "DH"],
                [29, "LF"],
                [3, "C"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 31, 36, 11, 19, 38, 22, 46],
        },
        "home": {
            "team": "Los Angeles Dodgers",
            "starter": 35,
            "roster": {
                # Lineup
                25: "Carl Crawford",
                7: "Nick Punto",
                23: "Adrián González",
                13: "Hanley Ramirez",
                66: "Yasiel Puig",
                55: "Skip Schumaker",
                17: "A.J. Ellis",
                5: "Juan Uribe",
                35: "Chris Capuano",
                # Starting pitcher
                35: "Chris Capuano",
                # Bench
                6: "Jerry Hairston",
                16: "Andre Ethier",
                18: "Tim Federowicz",
                14: "Mark Ellis",
                # Bullpen
                21: "Zack Greinke",
                43: "Brandon League",
                75: "Paco Rodríguez",
                56: "J.P. Howell",
                74: "Kenley Jansen",
                99: "Hyun Jin Ryu",
                22: "Clayton Kershaw",
                44: "Chris Withrow",
                49: "Carlos Marmol",
                0: "Brian Wilson",
                54: "Ronald Belisario",
                47: "Ricky Nolasco",
            },
            "lefties": [35, 75, 56, 99, 22],
            "lineup": [
                [25, "7"],
                [7, "4"],
                [23, "3"],
                [13, "6"],
                [66, "9"],
                [55, "8"],
                [17, "2"],
                [5, "5"],
                [35, "1"],
            ],
            "bench": [
                [6, "2B"],
                [16, "RF"],
                [18, "C"],
                [14, "2B"],
            ],
            "bullpen": [21, 43, 75, 56, 74, 99, 22, 44, 49, 0, 54, 47],
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
# Pitching: LAD #35 Chris Capuano
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c f b b s")
t1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(2)
t1.advance(3, "15 1B")
t1.advance(4, "12 2B")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b f b")
t1.hit(1)
t1.advance(3, "12 2B")

# 4. BOS #12 Mike Napoli (18 - X - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("s b b s 1 b")
t1.hit(2, rbis=1)

# 5. BOS #5  Jonny Gomes (15 - 12 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("i i i i")
t1.reach("IBB")
t1.thrown_out(2, "16 DP5-4-3", 2, 35)

# 6. BOS #16 Will Middlebrooks (15 - 12 - 5)
t1.new_ab(is_risp=True)
t1.pitch_list("f b b s")
t1.out("DP5-4-3")


# Bot 1st
# Pitching: BOS #44 Jake Peavy
b1 = game.new_inning()

# 1. LAD #25 Carl Crawford (X - X - X)
b1.new_ab()
b1.pitch_list("b f b f b s")
b1.out("K")

# 2. LAD #7  Nick Punto (X - X - X)
b1.new_ab()
b1.pitch_list("c f b s")
b1.out("K")

# 3. LAD #23 Adrián González (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAD #35 Chris Capuano
t2 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("c b f c")
t2.out("!K")

# 8. BOS #72 Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b")
t2.out("G5-3")

# 9. BOS #44 Jake Peavy (X - X - X)
t2.new_ab()
t2.pitch_list("f b")
t2.out("G6-3")


# Bot 2nd
# Pitching: BOS #44 Jake Peavy
b2 = game.new_inning()

# 4. LAD #13 Hanley Ramirez (X - X - X)
b2.new_ab()
b2.out("P3")

# 5. LAD #66 Yasiel Puig (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b f")
b2.out("G6-3")

# 6. LAD #55 Skip Schumaker (X - X - X)
b2.new_ab()
b2.pitch_list("b c f")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAD #35 Chris Capuano
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("b c c f b f")
t3.hit(1)
t3.advance(2, "18 SB")
t3.advance(3, "18 SAC1-3")
t3.advance(4, "15 SF8")

# 2. BOS #18 Shane Victorino (X - X - 2)
t3.new_ab(is_risp=True)
t3.pitch_list("b 1 b")
t3.out("SAC1-3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b f")
t3.out("SF8", rbis=1)

# 4. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #44 Jake Peavy
b3 = game.new_inning()

# 7. LAD #17 A.J. Ellis (X - X - X)
b3.new_ab()
b3.pitch_list("c b b s f f f f b b")
b3.reach("BB")
b3.advance(2, "35 SAC3")

# 8. LAD #5  Juan Uribe (X - X - 17)
b3.new_ab()
b3.pitch_list("b")
b3.out("F9")

# 9. LAD #35 Chris Capuano (X - X - 17)
b3.new_ab()
b3.pitch_list("l")
b3.out("SAC3")

# 1. LAD #25 Carl Crawford (X - 17 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f b b f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAD #35 Chris Capuano
t4 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("b s b f s")
t4.out("K")

# 6. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.error(8)
t4.advance(2, "72 1B")
t4.advance("U", "72 E8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 16)
t4.new_ab()
t4.pitch_list("s 1 b f")
t4.out("L5")

# 8. BOS #72 Xander Bogaerts (X - X - 16)
t4.new_ab()
t4.hit(1)
t4.advance(2, "E8")

# 9. BOS #44 Jake Peavy (X - 72 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #44 Jake Peavy
b4 = game.new_inning()

# 2. LAD #7  Nick Punto (X - X - X)
b4.new_ab()
b4.out("B4-3")

# 3. LAD #23 Adrián González (X - X - X)
b4.new_ab()
b4.pitch_list("c f")
b4.hit(4)

# 4. LAD #13 Hanley Ramirez (X - X - X)
b4.new_ab()
b4.pitch_list("b c c")
b4.out("G5-3")

# 5. LAD #66 Yasiel Puig (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAD #35 Chris Capuano
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("b c f")
t5.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c")
t5.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("f b")
t5.out("F8")


# Bot 5th
# Pitching: BOS #44 Jake Peavy
b5 = game.new_inning()

# 6. LAD #55 Skip Schumaker (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(1)

# 7. LAD #17 A.J. Ellis (X - X - 55)
b5.new_ab()
b5.pitch_list("c f f f b")
b5.out("F8")

# 8. LAD #5  Juan Uribe (X - X - 55)
b5.new_ab()
b5.pitch_list("1")
b5.out("L9")

# Offensive change (LAD): Pinch-hitter #16 Andre Ethier replaces #35 Chris Capuano, batting 9th
b5.offensive_substitution(9, 16, "PH")

# 9. LAD #16 Andre Ethier (X - X - 55)
b5.new_ab()
b5.pitch_list("c d s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAD #44 Chris Withrow
t6 = game.new_inning()

# Pitching change (LAD): #44 Chris Withrow replaces #35 Chris Capuano, batting 9th
t6.pitching_substitution(44)
t6.defensive_substitution(9, 44, "1")

# 4. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("t b b b s f b")
t6.reach("BB")
t6.advance(4, "39 HR")

# 5. BOS #5  Jonny Gomes (X - X - 12)
t6.new_ab()
t6.pitch_list("c b s")
t6.out("F9")

# 6. BOS #16 Will Middlebrooks (X - X - 12)
t6.new_ab()
t6.pitch_list("s s c")
t6.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
t6.new_ab()
t6.pitch_list("b f")
t6.hit(4, rbis=2)

# 8. BOS #72 Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("b s s f b")
t6.out("L3")


# Bot 6th
# Pitching: BOS #44 Jake Peavy
b6 = game.new_inning()

# 1. LAD #25 Carl Crawford (X - X - X)
b6.new_ab()
b6.pitch_list("b s")
b6.hit(1)

# 2. LAD #7  Nick Punto (X - X - 25)
b6.new_ab()
b6.out("(F)P5")

# 3. LAD #23 Adrián González (X - X - 25)
b6.new_ab()
b6.pitch_list("s")
b6.out("F9")

# 4. LAD #13 Hanley Ramirez (X - X - 25)
b6.new_ab()
b6.pitch_list("d b f")
b6.out("(F)P2")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAD #44 Chris Withrow
t7 = game.new_inning()

# 9. BOS #44 Jake Peavy (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("L9")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("b b f c f f f f f f")
t7.out("F9")

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c b t")
t7.hit(1)

# 4. BOS #12 Mike Napoli (X - X - 15)
t7.new_ab()
t7.pitch_list("c d b b s")
t7.out("P4")


# Bot 7th
# Pitching: BOS #44 Jake Peavy
b7 = game.new_inning()

# 5. LAD #66 Yasiel Puig (X - X - X)
b7.new_ab()
b7.pitch_list("s s")
b7.out("G5-3")

# 6. LAD #55 Skip Schumaker (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("L8")

# 7. LAD #17 A.J. Ellis (X - X - X)
b7.new_ab()
b7.pitch_list("c b b f b")
b7.out("P4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAD #49 Carlos Marmol
t8 = game.new_inning()

# Pitching change (LAD): #49 Carlos Marmol replaces #44 Chris Withrow, batting 9th
t8.pitching_substitution(49)
t8.defensive_substitution(9, 49, "1")

# 5. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.out("(F)P3")

# 6. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("c b s b s")
t8.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("b f b f f f b b")
t8.reach("BB")
t8.advance(3, "72 1B")

# 8. BOS #72 Xander Bogaerts (X - X - 39)
t8.new_ab()
t8.pitch_list("c s")
t8.hit(1)

# 9. BOS #44 Jake Peavy (39 - X - 72)
t8.new_ab(is_risp=True)
t8.out("L1")


# Bot 8th
# Pitching: BOS #44 Jake Peavy
b8 = game.new_inning()

# 8. LAD #5  Juan Uribe (X - X - X)
b8.new_ab()
b8.pitch_list("f f")
b8.out("G3")

# Offensive change (LAD): Pinch-hitter #6 Jerry Hairston replaces #49 Carlos Marmol, batting 9th
b8.offensive_substitution(9, 6, "PH")

# 9. LAD #6  Jerry Hairston (X - X - X)
b8.new_ab()
b8.pitch_list("c b b t f")
b8.out("G6-3")

# 1. LAD #25 Carl Crawford (X - X - X)
b8.new_ab()
b8.pitch_list("f b f b")
b8.out("L8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAD #43 Brandon League
t9 = game.new_inning()

# Pitching change (LAD): #43 Brandon League replaces #49 Carlos Marmol, batting 9th
t9.pitching_substitution(43)
t9.defensive_substitution(9, 43, "1")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("L4")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("b c b f b s")
t9.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c s b b b")
t9.hit(2)
t9.advance(4, "12 HR")

# 4. BOS #12 Mike Napoli (X - 15 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b f d b f f f")
t9.hit(4, rbis=2)

# 5. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")


# Bot 9th
# Pitching: BOS #44 Jake Peavy
b9 = game.new_inning()

# 2. LAD #7  Nick Punto (X - X - X)
b9.new_ab()
b9.pitch_list("b c c")
b9.out("L8")

# 3. LAD #23 Adrián González (X - X - X)
b9.new_ab()
b9.out("L7")

# 4. LAD #13 Hanley Ramirez (X - X - X)
b9.new_ab()
b9.pitch_list("c f b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #44 Jake Peavy
game.winning_pitcher(44, is_away_team=True)

# Loser team: LAD
# LP: LAD #35 Chris Capuano
game.losing_pitcher(35)

# print(game)
game.generate_scorecard()
