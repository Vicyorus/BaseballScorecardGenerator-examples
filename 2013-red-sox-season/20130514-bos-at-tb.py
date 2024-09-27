import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-05-14
# https://www.baseball-reference.com/boxes/TBA/TBA201305140.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/05/14/347318/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-14 19:11-22:25",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "15,227",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                20: "Ryan Lavarnway",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [16, "5"],
                [7, "6"],
                [20, "2"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
                [23, "3B"],
            ],
            "bullpen": [63, 65, 30, 32, 31, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 55,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                20: "Matt Joyce",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                21: "James Loney",
                30: "Luke Scott",
                2: "Kelly Johnson",
                28: "José Molina",
                11: "Yunel Escobar",
                # Starting pitcher
                55: "Matt Moore",
                # Bench
                1: "Sean Rodríguez",
                19: "Ryan Roberts",
                59: "Jose Lobaton",
                5: "Sam Fuld",
                # Bullpen
                58: "Jeremy Hellickson",
                53: "Alex Cobb",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                27: "Cesár Ramos",
                52: "Josh Lueke",
                14: "David Price",
                56: "Fernando Rodney",
                40: "Roberto Hernandez",
            },
            "lefties": [55, 57, 27, 14],
            "lineup": [
                [8, "8"],
                [20, "7"],
                [18, "9"],
                [3, "5"],
                [21, "3"],
                [30, "0"],
                [2, "4"],
                [28, "2"],
                [11, "6"],
            ],
            "bench": [
                [1, "2B"],
                [19, "3B"],
                [59, "C"],
                [5, "LF"],
            ],
            "bullpen": [58, 53, 62, 35, 43, 57, 27, 52, 14, 56, 40],
        },
        "umpires": {
            "HP": "Rob Drake",
            "1B": "Sam Holbrook",
            "2B": "Joe West",
            "3B": "David Rackley",
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
# Pitching: TBR #55 Matt Moore
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b")
t1.reach("HBP")
t1.advance(3, "15 2B")
t1.advance(4, "34 HR")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("c b c f d 1 f 1 t")
t1.out("KT")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t1.new_ab()
t1.pitch_list("b 1 1 c")
t1.hit(2)
t1.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (2 - 15 - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(4, rbis=3)

# 5. BOS #12 Mike Napoli (X - X - X)
t1.new_ab()
t1.pitch_list("b c b f b")
t1.out("G5-3")

# 6. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("s f f b f f c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
b1.new_ab()
b1.pitch_list("c b f f b s")
b1.out("K")

# 2. TBR #20 Matt Joyce (X - X - X)
b1.new_ab()
b1.pitch_list("c c b")
b1.out("F8")

# 3. TBR #18 Ben Zobrist (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #55 Matt Moore
t2 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("b c f s")
t2.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b c")
t2.out("!K")

# 9. BOS #20 Ryan Lavarnway (X - X - X)
t2.new_ab()
t2.pitch_list("b s b f f c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
b2.new_ab()
b2.pitch_list("c f t")
b2.out("KT")

# 5. TBR #21 James Loney (X - X - X)
b2.new_ab()
b2.out("F8")

# 6. TBR #30 Luke Scott (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #55 Matt Moore
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.out("P4")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F8")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 7. TBR #2  Kelly Johnson (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("G4-3")

# 8. TBR #28 José Molina (X - X - X)
b3.new_ab()
b3.pitch_list("f f b")
b3.hit(1)
b3.advance(3, "11 2B")

# 9. TBR #11 Yunel Escobar (X - X - 28)
b3.new_ab()
b3.hit(2)

# 1. TBR #8  Desmond Jennings (28 - 11 - X)
b3.new_ab()
b3.pitch_list("b b b c")
b3.out("L5")

# 2. TBR #20 Matt Joyce (28 - 11 - X)
b3.new_ab()
b3.pitch_list("b b b c b")
b3.reach("BB")

# 3. TBR #18 Ben Zobrist (28 - 11 - 20)
b3.new_ab()
b3.pitch_list("c b f f")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #55 Matt Moore
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b c b")
t4.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b b s c f c")
t4.out("!K")

# 6. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("s b")
t4.out("P3")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
b4.new_ab()
b4.pitch_list("f f b b f b f")
b4.hit(1)
b4.advance(3, "21 1B")
b4.advance(4, "30 2B")

# 5. TBR #21 James Loney (X - X - 3)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.advance(3, "30 2B")
b4.advance(4, "28 1B")

# 6. TBR #30 Luke Scott (3 - X - 21)
b4.new_ab()
b4.pitch_list("b")
b4.hit(2, rbis=1)
b4.advance(4, "28 1B")

# 7. TBR #2  Kelly Johnson (21 - 30 - X)
b4.new_ab()
b4.pitch_list("b f s f d s")
b4.out("K")

# 8. TBR #28 José Molina (21 - 30 - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.hit(1, rbis=2)
b4.advance(2, "11 1B")
b4.advance(3, "8 F8")
b4.advance(4, "20 1B")

# 9. TBR #11 Yunel Escobar (X - X - 28)
b4.new_ab()
b4.hit(1)
b4.advance(2, "8 F8")
b4.advance(4, "20 1B")

# 1. TBR #8  Desmond Jennings (X - 28 - 11)
b4.new_ab()
b4.pitch_list("c b b b")
b4.out("F8")

# 2. TBR #20 Matt Joyce (28 - 11 - X)
b4.new_ab()
b4.pitch_list("s")
b4.hit(1, rbis=2)
b4.advance(2, "18 SB")

# 3. TBR #18 Ben Zobrist (X - X - 20)
b4.new_ab()
b4.pitch_list("1 c b b c")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #55 Matt Moore
t5 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c f b")
t5.out("P4")

# 8. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.hit(2)

# 9. BOS #20 Ryan Lavarnway (X - 7 - X)
t5.new_ab()
t5.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - X)
t5.new_ab()
t5.pitch_list("b f b f f f d b")
t5.reach("BB")

# 2. BOS #18 Shane Victorino (X - 7 - 2)
t5.new_ab()
t5.pitch_list("c")
t5.out("F9")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
b5.new_ab()
b5.pitch_list("f f")
b5.out("G5-3")

# 5. TBR #21 James Loney (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(2)
b5.thrown_out(3, "30 CS", 3, 30)

# Pitching change (BOS): #30 Andrew Miller replaces #41 John Lackey
b5.pitching_substitution(30)

# 6. TBR #30 Luke Scott (X - 21 - X)
b5.new_ab()
b5.pitch_list("c b c b b s")
b5.out("KDP2")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #55 Matt Moore
t6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
t6.new_ab()
t6.pitch_list("1")
t6.out("F7")

# 5. BOS #12 Mike Napoli (X - X - 15)
t6.new_ab()
t6.pitch_list("1 b c b s f s")
t6.out("K")

# 6. BOS #5  Jonny Gomes (X - X - 15)
t6.new_ab()
t6.pitch_list("d c s s")
t6.out("K")


# Bot 6th
# Pitching: BOS #30 Andrew Miller
b6 = game.new_inning()

# 7. TBR #2  Kelly Johnson (X - X - X)
b6.new_ab()
b6.hit(1)
b6.advance(2, "28 SAC1-4")

# Pitching change (BOS): #59 Clayton Mortensen replaces #30 Andrew Miller
b6.pitching_substitution(59)

# 8. TBR #28 José Molina (X - X - 2)
b6.new_ab()
b6.pitch_list("1")
b6.out("SAC1-4")

# 9. TBR #11 Yunel Escobar (X - 2 - X)
b6.new_ab()
b6.pitch_list("b c b b f f b")
b6.reach("BB")

# 1. TBR #8  Desmond Jennings (X - 2 - 11)
b6.new_ab()
b6.pitch_list("b b c")
b6.out("F9")

# 2. TBR #20 Matt Joyce (X - 2 - 11)
b6.new_ab()
b6.pitch_list("c b b")
b6.out("L9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #57 Jake McGee
t7 = game.new_inning()

# Pitching change (TBR): #57 Jake McGee replaces #55 Matt Moore
t7.pitching_substitution(57)

# 7. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b s b c f b f f f")
t7.out("G6-3")

# 8. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("b f b b b")
t7.reach("BB")
t7.advance(2, "2 BB")

# 9. BOS #20 Ryan Lavarnway (X - X - 7)
t7.new_ab()
t7.pitch_list("f b b c b")
t7.out("L9")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
t7.new_ab()
t7.pitch_list("c b d 1 b f b")
t7.reach("BB")

# Pitching change (TBR): #52 Josh Lueke replaces #57 Jake McGee
t7.pitching_substitution(52)

# 2. BOS #18 Shane Victorino (X - 7 - 2)
t7.new_ab()
t7.pitch_list("c c f b f b")
t7.out("L3")


# Bot 7th
# Pitching: BOS #59 Clayton Mortensen
b7 = game.new_inning()

# 3. TBR #18 Ben Zobrist (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F8")

# 4. TBR #3  Evan Longoria (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("F9")

# Pitching change (BOS): #32 Craig Breslow replaces #59 Clayton Mortensen
b7.pitching_substitution(32)

# 5. TBR #21 James Loney (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #62 Joel Peralta
t8 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #52 Josh Lueke
t8.pitching_substitution(62)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c b s f b f b")
t8.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("c c t")
t8.out("KT")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# 6. TBR #30 Luke Scott (X - X - X)
b8.new_ab()
b8.out("G3")

# 7. TBR #2  Kelly Johnson (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f b s")
b8.out("K")

# 8. TBR #28 José Molina (X - X - X)
b8.new_ab()
b8.pitch_list("f s f b")
b8.hit(2)

# Pitching change (BOS): #63 Alex Wilson replaces #32 Craig Breslow
b8.pitching_substitution(63)

# 9. TBR #11 Yunel Escobar (X - 28 - X)
b8.new_ab()
b8.pitch_list("c b s b")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #56 Fernando Rodney
t9 = game.new_inning()

# Pitching change (TBR): #56 Fernando Rodney replaces #62 Joel Peralta
t9.pitching_substitution(56)

# Defensive change (TBR): #19 Ryan Roberts replaces #2 Kelly Johnson (2B), playing 2B, batting 7th
t9.defensive_substitution(7, 19, "4")

# 6. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("c t s")
t9.out("K")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("b b s c b f f s")
t9.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c s b b s")
t9.out("K")

# Winning team: TBR
# WP: TBR #55 Matt Moore
game.winning_pitcher(55)
# SV: TBR #56 Fernando Rodney
game.save_pitcher(56)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
