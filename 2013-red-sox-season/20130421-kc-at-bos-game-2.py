import os
from baseball_scorecard.baseball_scorecard import Scorecard

# KC @ BOS, 2013-04-21
# https://www.baseball-reference.com/boxes/BOS/BOS201304212.shtml
# https://www.mlb.com/gameday/royals-vs-red-sox/2013/04/21/346981/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-21 19:06-22:17",
        "at": "Fenway Park, Boston, MA",
        "att": "33,270",
        "temp": "47F, Clear",
        "wind": "13mph, In From RF",
        "away": {
            "team": "Kansas City Royals",
            "starter": 11,
            "roster": {
                # Lineup
                4: "Alex Gordon",
                2: "Alcides Escobar",
                16: "Billy Butler",
                35: "Eric Hosmer",
                6: "Lorenzo Cain",
                8: "Mike Moustakas",
                21: "Jeff Francoeur",
                26: "George Kottaras",
                23: "Elliot Johnson",
                # Starting pitcher
                11: "Jeremy Guthrie",
                # Bench
                17: "Chris Getz",
                13: "Salvador Perez",
                24: "Miguel Tejada",
                1: "Jarrod Dyson",
                # Bullpen
                56: "Greg Holland",
                54: "Ervin Santana",
                33: "James Shields",
                27: "Juan Gutierrez",
                52: "Bruce Chen",
                39: "Luis Mendoza",
                22: "Wade Davis",
                40: "Kelvin Herrera",
                53: "Will Smith",
                43: "Aaron Crow",
                44: "Luke Hochevar",
                55: "Tim Collins",
            },
            "lefties": [52, 53, 55],
            "lineup": [
                [4, "7"],
                [2, "6"],
                [16, "0"],
                [35, "3"],
                [6, "8"],
                [8, "5"],
                [21, "9"],
                [26, "2"],
                [23, "4"],
            ],
            "bench": [
                [17, "2B"],
                [13, "C"],
                [24, "SS"],
                [1, "CF"],
            ],
            "bullpen": [56, 54, 33, 27, 52, 39, 22, 40, 53, 43, 44, 55],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 64,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                37: "Mike Carp",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Starting pitcher
                64: "Allen Webster",
                # Bench
                7: "Stephen Drew",
                34: "David Ortiz",
                18: "Shane Victorino",
                5: "Jonny Gomes",
                # Bullpen
                63: "Alex Wilson",
                35: "Steven Wright",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [12, "3"],
                [39, "0"],
                [16, "5"],
                [37, "7"],
                [3, "2"],
                [23, "6"],
            ],
            "bench": [
                [7, "SS"],
                [34, "DH"],
                [18, "CF"],
                [5, "LF"],
            ],
            "bullpen": [63, 35, 40, 30, 91, 31, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Tony Randazzo",
            "1B": "Manny Gonzalez",
            "2B": "Wally Bell",
            "3B": "Lance Barrett",
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
# Pitching: BOS #64 Allen Webster
t1 = game.new_inning()

# 1. KCR #4  Alex Gordon (X - X - X)
t1.new_ab()
t1.hit(2)
t1.error(6)
t1.advance("U", "2 E6")

# 2. KCR #2  Alcides Escobar (X - 4 - X)
t1.new_ab()
t1.pitch_list("s b")
t1.hit(1)
t1.advance(2, "E6")

# 3. KCR #16 Billy Butler (X - 2 - X)
t1.new_ab()
t1.pitch_list("b c b c f s")
t1.out("K")

# 4. KCR #35 Eric Hosmer (X - 2 - X)
t1.new_ab()
t1.pitch_list("f f b s")
t1.out("K")

# 5. KCR #6  Lorenzo Cain (X - 2 - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")


# Bot 1st
# Pitching: KCR #11 Jeremy Guthrie
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.advance(2, "29 WP")
b1.thrown_out(2, "29 DP3-6", 2, 11)

# 2. BOS #29 Daniel Nava (X - X - 2)
b1.new_ab()
b1.pitch_list("c b s")
b1.wp()
b1.out("DP3-6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b f b c")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #64 Allen Webster
t2 = game.new_inning()

# 6. KCR #8  Mike Moustakas (X - X - X)
t2.new_ab()
t2.pitch_list("c b f")
t2.out("G4-3")

# 7. KCR #21 Jeff Francoeur (X - X - X)
t2.new_ab()
t2.pitch_list("f b b")
t2.out("P4")

# 8. KCR #26 George Kottaras (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G4-3")


# Bot 2nd
# Pitching: KCR #11 Jeremy Guthrie
b2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("s f b")
b2.hit(4)

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")
b2.advance(4, "37 2B")

# 6. BOS #16 Will Middlebrooks (X - X - 39)
b2.new_ab()
b2.pitch_list("s c f b")
b2.out("P6")

# 7. BOS #37 Mike Carp (X - X - 39)
b2.new_ab()
b2.pitch_list("b b f b")
b2.hit(2, rbis=1)

# 8. BOS #3  David Ross (X - 37 - X)
b2.new_ab()
b2.pitch_list("c c t")
b2.out("KT")

# 9. BOS #23 Pedro Ciriaco (X - 37 - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #64 Allen Webster
t3 = game.new_inning()

# 9. KCR #23 Elliot Johnson (X - X - X)
t3.new_ab()
t3.pitch_list("b f s c")
t3.out("!K")

# 1. KCR #4  Alex Gordon (X - X - X)
t3.new_ab()
t3.out("G3-1")

# 2. KCR #2  Alcides Escobar (X - X - X)
t3.new_ab()
t3.pitch_list("c s")
t3.hit(1)

# 3. KCR #16 Billy Butler (X - X - 2)
t3.new_ab()
t3.out("P4")


# Bot 3rd
# Pitching: KCR #11 Jeremy Guthrie
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.hit(2)
b3.advance(3, "29 G4-3")
b3.advance(4, "15 1B")

# 2. BOS #29 Daniel Nava (X - 2 - X)
b3.new_ab()
b3.pitch_list("f b b")
b3.out("G4-3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.hit(1, rbis=1)
b3.thrown_out(2, "12 CS", 2, 11)

# 4. BOS #12 Mike Napoli (X - X - 15)
b3.new_ab()
b3.pitch_list("c f b p f")
b3.hit(2)
b3.thrown_out(4, "39 4-2-5-2-6", 3, 11)

# 5. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
b3.new_ab()
b3.hit(1)


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #64 Allen Webster
t4 = game.new_inning()

# 4. KCR #35 Eric Hosmer (X - X - X)
t4.new_ab()
t4.pitch_list("c s b")
t4.out("G5-3")

# 5. KCR #6  Lorenzo Cain (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.reach("HBP")
t4.thrown_out(2, "8 CS", 2, 64)

# 6. KCR #8  Mike Moustakas (X - X - 6)
t4.new_ab()
t4.pitch_list("1 1 b")
t4.out("F9")


# Bot 4th
# Pitching: KCR #11 Jeremy Guthrie
b4 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("c c")
b4.out("G1-3")

# 7. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b f")
b4.hit(3)

# 8. BOS #3  David Ross (37 - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G5-3")

# 9. BOS #23 Pedro Ciriaco (37 - X - X)
b4.new_ab()
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #64 Allen Webster
t5 = game.new_inning()

# 7. KCR #21 Jeff Francoeur (X - X - X)
t5.new_ab()
t5.pitch_list("b c b s b f f s")
t5.out("K")

# 8. KCR #26 George Kottaras (X - X - X)
t5.new_ab()
t5.pitch_list("c b b")
t5.hit(4)

# 9. KCR #23 Elliot Johnson (X - X - X)
t5.new_ab()
t5.pitch_list("c s s")
t5.out("K")

# 1. KCR #4  Alex Gordon (X - X - X)
t5.new_ab()
t5.pitch_list("c b b c")
t5.hit(4)

# 2. KCR #2  Alcides Escobar (X - X - X)
t5.new_ab()
t5.pitch_list("f s")
t5.out("G1-3")


# Bot 5th
# Pitching: KCR #11 Jeremy Guthrie
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("c c b")
b5.out("L7")

# 2. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b f b c b f b")
b5.reach("BB")
b5.advance(2, "15 1B")
b5.advance(4, "12 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b5.new_ab()
b5.pitch_list("b f b c")
b5.hit(1)
b5.advance(3, "12 1B")

# 4. BOS #12 Mike Napoli (X - 29 - 15)
b5.new_ab()
b5.pitch_list("f c f f")
b5.hit(1, rbis=1)
b5.advance(2, "39 PB")

# 5. BOS #39 Jarrod Saltalamacchia (15 - X - 12)
b5.new_ab()
b5.pitch_list("b b s s s")
b5.pb()
b5.out("K")

# 6. BOS #16 Will Middlebrooks (15 - 12 - X)
b5.new_ab()
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #64 Allen Webster
t6 = game.new_inning()

# 3. KCR #16 Billy Butler (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b b")
t6.reach("BB")
t6.thrown_out(2, "35 FC4-6", 1, 64)

# 4. KCR #35 Eric Hosmer (X - X - 16)
t6.new_ab()
t6.pitch_list("s")
t6.reach("FC4-6")

# 5. KCR #6  Lorenzo Cain (X - X - 35)
t6.new_ab()
t6.pitch_list("b 1 s s f b")
t6.out("L4")

# 6. KCR #8  Mike Moustakas (X - X - 35)
t6.new_ab()
t6.pitch_list("f f b")
t6.out("P4")


# Bot 6th
# Pitching: KCR #11 Jeremy Guthrie
b6 = game.new_inning()

# 7. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G4-3")

# 8. BOS #3  David Ross (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c f f")
b6.out("L9")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
b6.new_ab()
b6.pitch_list("c c f b b f f b f b")
b6.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
b6.new_ab()
b6.pitch_list("b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #36 Junichi Tazawa
t7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #64 Allen Webster
t7.pitching_substitution(36)

# 7. KCR #21 Jeff Francoeur (X - X - X)
t7.new_ab()
t7.pitch_list("c s b b f b f")
t7.out("L4")

# 8. KCR #26 George Kottaras (X - X - X)
t7.new_ab()
t7.pitch_list("b b c c s")
t7.out("K")

# 9. KCR #23 Elliot Johnson (X - X - X)
t7.new_ab()
t7.pitch_list("c s f b s")
t7.out("K")


# Bot 7th
# Pitching: KCR #44 Luke Hochevar
b7 = game.new_inning()

# Pitching change (KCR): #44 Luke Hochevar replaces #11 Jeremy Guthrie
b7.pitching_substitution(44)

# 2. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c b f")
b7.out("L7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b b b")
b7.reach("BB")
b7.advance(2, "39 SB")

# 4. BOS #12 Mike Napoli (X - X - 15)
b7.new_ab()
b7.pitch_list("b")
b7.out("L7")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - 15)
b7.new_ab()
b7.pitch_list("b c c")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t8.pitching_substitution(19)

# 1. KCR #4  Alex Gordon (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("G5-3")

# 2. KCR #2  Alcides Escobar (X - X - X)
t8.new_ab()
t8.pitch_list("b f b s f")
t8.out("F8")

# 3. KCR #16 Billy Butler (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(4)

# 4. KCR #35 Eric Hosmer (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b")
t8.hit(1)

# 5. KCR #6  Lorenzo Cain (X - X - 35)
t8.new_ab()
t8.pitch_list("c b f 1 c")
t8.out("!K")


# Bot 8th
# Pitching: KCR #40 Kelvin Herrera
b8 = game.new_inning()

# Pitching change (KCR): #40 Kelvin Herrera replaces #44 Luke Hochevar
b8.pitching_substitution(40)

# 6. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("b b s b")
b8.out("G6-3")

# 7. BOS #37 Mike Carp (X - X - X)
b8.new_ab()
b8.pitch_list("c s f f b b s")
b8.out("K")

# 8. BOS #3  David Ross (X - X - X)
b8.new_ab()
b8.out("G3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
t9.pitching_substitution(40)

# 6. KCR #8  Mike Moustakas (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F8")

# 7. KCR #21 Jeff Francoeur (X - X - X)
t9.new_ab()
t9.pitch_list("s b c b s")
t9.out("K")

# 8. KCR #26 George Kottaras (X - X - X)
t9.new_ab()
t9.pitch_list("c s c")
t9.out("!K")


# Bot 9th
# Pitching: KCR #40 Kelvin Herrera
b9 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
b9.new_ab()
b9.pitch_list("f s f s")
b9.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b9.new_ab()
b9.pitch_list("b f")
b9.hit(1)
b9.advance(2, "29 SB")

# 2. BOS #29 Daniel Nava (X - X - 2)
b9.new_ab()
b9.pitch_list("b c b f f b s")
b9.out("K")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b9.new_ab()
b9.pitch_list("i i i i")
b9.reach("IBB")

# 4. BOS #12 Mike Napoli (X - 2 - 15)
b9.new_ab()
b9.pitch_list("f s")
b9.out("F8")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #30 Andrew Miller
t10 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #40 Andrew Bailey
t10.pitching_substitution(30)

# Offensive change (KCR): Pinch-hitter #24 Miguel Tejada replaces #23 Elliot Johnson, batting 9th
t10.offensive_substitution(9, 24, "PH")

# 9. KCR #24 Miguel Tejada (X - X - X)
t10.new_ab()
t10.pitch_list("f b f f c")
t10.out("!K")

# 1. KCR #4  Alex Gordon (X - X - X)
t10.new_ab()
t10.pitch_list("b f f f b")
t10.hit(1)
t10.advance(2, "2 BB")
t10.advance(3, "35 1B")
t10.advance(4, "6 BB")

# 2. KCR #2  Alcides Escobar (X - X - 4)
t10.new_ab()
t10.pitch_list("b b b b")
t10.reach("BB")
t10.advance(2, "35 1B")
t10.advance(3, "6 BB")

# 3. KCR #16 Billy Butler (X - 4 - 2)
t10.new_ab()
t10.pitch_list("b c f b s")
t10.out("K")

# 4. KCR #35 Eric Hosmer (X - 4 - 2)
t10.new_ab()
t10.pitch_list("b c")
t10.hit(1)
t10.advance(2, "6 BB")

# 5. KCR #6  Lorenzo Cain (4 - 2 - 35)
t10.new_ab()
t10.pitch_list("b b b b")
t10.reach("BB", rbis=1)

# 6. KCR #8  Mike Moustakas (2 - 35 - 6)
t10.new_ab()
t10.pitch_list("c")
t10.out("G3-1")


# Bot 10th
# Pitching: KCR #56 Greg Holland
b10 = game.new_inning()

# Pitching change (KCR): #56 Greg Holland replaces #40 Kelvin Herrera
b10.pitching_substitution(56)

# Defensive change (KCR): #13 Salvador Perez replaces #26 George Kottaras (C), playing C, batting 8th
b10.defensive_substitution(8, 13, "2")

# Defensive change (KCR): #17 Chris Getz replaces #24 Miguel Tejada (PH), playing 2B, batting 9th
b10.defensive_substitution(9, 17, "4")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
b10.new_ab()
b10.pitch_list("s f s")
b10.out("K")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b10.new_ab()
b10.pitch_list("s c b f f b b s")
b10.out("K")

# 7. BOS #37 Mike Carp (X - X - X)
b10.new_ab()
b10.pitch_list("c s s")
b10.out("K")

# Winning team: KCR
# WP: KCR #40 Kelvin Herrera
game.winning_pitcher(40, is_away_team=True)
# SV: KCR #56 Greg Holland
game.save_pitcher(56, is_away_team=True)

# Loser team: BOS
# LP: BOS #30 Andrew Miller
game.losing_pitcher(30)

# print(game)
game.generate_scorecard()
