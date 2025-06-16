import tkinter as tk
from tkinter import ttk
import copy

# --- GUI constants ---
ROW_HEIGHT = 20
LEFT_MARGIN = 170
RIGHT_MARGIN = 170
FONT_MAIN = ("Helvetica", 9)
FONT_DIV = ("Helvetica", 10, "bold")
BG_COLOUR = "#0D1117"
TEXT_COLOUR = "#C9D1D9"
LINE_COLOUR = "#8B949E"
DIVIDER_LINE_COLOUR = "#8B949E" 
HIGHLIGHT_COLOUR = "#FFFF00"

# --- Blade representations ---
BLADE_COLOURS = {
    'Caius': ['#000000', '#00FFFF', '#000000', '#000000', '#000000'],
    'Christ\'s': ['#000080', '#FFFFFF', '#000080', '#FFFFFF', '#000080'],
    'Churchill': ['#FF69B4'],
    'Clare': ['#FFD700'],
    'Clare Hall': ['#FFD700', '#000000', '#DC143C'],
    'Corpus Christi': ['#A52A2A', '#FFFFFF', '#A52A2A'],
    'Darwin': ['#000080', '#DC143C', '#000080', '#FFD700'],
    'Downing': ['#bd2375'],
    'Emmanuel': ['#00008B', '#FF0000', '#00008B'],
    'First and Third': ['#000080', '#FFD700'],
    'Fitzwilliam': ['#808080', '#DC143C', '#808080'],
    'Girton': ['#006400', '#FFFFFF', '#DC143C', '#FFFFFF', '#006400'],
    'Homerton': ['#FFFFFF', '#0000CD', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
    'Hughes Hall': ['#FFFFFF', '#00008B', '#FFFFFF', '#87CEEB', '#FFFFFF'],
    'Jesus': ['#000000', '#DC143C', '#000000', '#DC143C', '#000000'],
    'King\'s': ['#6A0DAD'],
    'Lady Margaret': ['#DC143C'],
    'Lucy Cavendish': ['#0000CD', '#000000', '#0000CD'],
    'Magdalene': ['#D8BFD8'],
    'Murray Edwards': ['#FFFFFF'],
    'Newnham': ['#000080', '#FFD700', '#FFFFFF', '#FFD700', '#000080'],
    'Pembroke': ['#87CEEB', '#00008B', '#87CEEB'],
    'Peterhouse': ['#0000CD', '#FFFFFF', '#0000CD', '#FFFFFF', '#0000CD'],
    'Queens\'': ['#006400', '#FFFFFF', '#006400'],
    'Robinson': ['#0000CD', '#FFD700', '#0000CD', '#FFD700', '#0000CD'],
    'Selwyn': ['#FFFFFF', '#FFD700', '#DC143C'],
    'Sidney Sussex': ['#000080', '#DC143C'],
    'St. Catharine\'s': ['#8B0000'],
    'St. Edmund\'s': ['#007ed6', '#FFFFFF', '#007ed6', '#00adff', '#007ed6'],
    'Trinity Hall': ['#000000'],
    'Wolfson': ['#4169E1', '#FFD700', '#4169E1'],

    # --- Aliases for all other boats, and matching colours ---
    'Caius II': ['#000000', '#00FFFF', '#000000', '#000000', '#000000'], 'Caius III': ['#000000', '#00FFFF', '#000000', '#000000', '#000000'],
    'Christ\'s II': ['#000080', '#FFFFFF', '#000080', '#FFFFFF', '#000080'],
    'Churchill II': ['#FF69B4'], 'Churchill III': ['#FF69B4'], 'Churchill IV': ['#FF69B4'],
    'Clare II': ['#FFD700'], 'Clare III': ['#FFD700'], 'Clare IV': ['#FFD700'],
    'Clare Hall II': ['#FFD700', '#000000', '#DC143C'],
    'Corpus Christi II': ['#A52A2A', '#FFFFFF', '#A52A2A'],
    'Darwin II': ['#000080', '#DC143C', '#000080', '#FFD700'],
    'Downing II': ['#bd2375'], 'Downing III': ['#bd2375'],
    'Emmanuel II': ['#00008B', '#FF0000', '#00008B'], 'Emmanuel III': ['#00008B', '#FF0000', '#00008B'], 'Emmanuel IV': ['#00008B', '#FF0000', '#00008B'],
    'First and Third II': ['#000080', '#FFD700'], 'First and Third III': ['#000080', '#FFD700'], 'First and Third IV': ['#000080', '#FFD700'],
    'Fitzwilliam II': ['#808080', '#DC143C', '#808080'], 'Fitzwilliam III': ['#808080', '#DC143C', '#808080'],
    'Girton II': ['#006400', '#FFFFFF', '#DC143C', '#FFFFFF', '#006400'],
    'Homerton II': ['#FFFFFF', '#0000CD', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 'Homerton III': ['#FFFFFF', '#0000CD', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
    'Hughes Hall II': ['#FFFFFF', '#00008B', '#FFFFFF', '#87CEEB', '#FFFFFF'], 'Hughes Hall III': ['#FFFFFF', '#00008B', '#FFFFFF', '#87CEEB', '#FFFFFF'],
    'Jesus II': ['#000000', '#DC143C', '#000000', '#DC143C', '#000000'], 'Jesus III': ['#000000', '#DC143C', '#000000', '#DC143C', '#000000'], 'Jesus IV': ['#000000', '#DC143C', '#000000', '#DC143C', '#000000'],
    'King\'s II': ['#6A0DAD'], 'King\'s III': ['#6A0DAD'],
    'Lady Margaret II': ['#DC143C'], 'Lady Margaret III': ['#DC143C'], 'Lady Margaret IV': ['#DC143C'],
    'Lucy Cavendish II': ['#0000CD', '#000000', '#0000CD'],
    'Magdalene II': ['#D8BFD8'], 'Magdalene III': ['#D8BFD8'],
    'Murray Edwards II': ['#FFFFFF'], 'Murray Edwards III': ['#FFFFFF'],
    'Newnham II': ['#000080', '#FFD700', '#FFFFFF', '#FFD700', '#000080'], 'Newnham III': ['#000080', '#FFD700', '#FFFFFF', '#FFD700', '#000080'],
    'Pembroke II': ['#87CEEB', '#00008B', '#87CEEB'], 'Pembroke III': ['#87CEEB', '#00008B', '#87CEEB'],
    'Peterhouse II': ['#0000CD', '#FFFFFF', '#0000CD', '#FFFFFF', '#0000CD'], 'Peterhouse III': ['#0000CD', '#FFFFFF', '#0000CD', '#FFFFFF', '#0000CD'], 'Peterhouse IV': ['#0000CD', '#FFFFFF', '#0000CD', '#FFFFFF', '#0000CD'],
    'Queens\' II': ['#006400', '#FFFFFF', '#006400'], 'Queens\' III': ['#006400', '#FFFFFF', '#006400'],
    'Robinson II': ['#0000CD', '#FFD700', '#0000CD', '#FFD700', '#0000CD'],
    'Selwyn II': ['#FFFFFF', '#FFD700', '#DC143C'], 'Selwyn III': ['#FFFFFF', '#FFD700', '#DC143C'],
    'Sidney Sussex II': ['#000080', '#DC143C'], 'Sidney Sussex III': ['#000080', '#DC143C'],
    'St. Catharine\'s II': ['#8B0000'], 'St. Catharine\'s III': ['#8B0000'],
    'St. Edmund\'s II': ['#007ed6', '#FFFFFF', '#007ed6', '#00adff', '#007ed6'],
    'Trinity Hall II': ['#000000'], 'Trinity Hall III': ['#000000'],
    'Wolfson II': ['#4169E1', '#FFD700', '#4169E1'],
}

MEN_START_ORDER_2025 = """
Division 1
1	Lady Margaret
2	Magdalene
3	Caius
4	Jesus
5	King's
6	Emmanuel
7	Downing
8	Pembroke
9	St. Catharine's
10	Peterhouse
11	Selwyn
12	Lady Margaret II
13	Clare
14	Hughes Hall
15	Queens'
16	Fitzwilliam
17	Robinson
Division 2
1	Caius II
2	First and Third
3	Wolfson
4	Churchill
5	Trinity Hall
6	Christ's
7	Corpus Christi
8	Girton
9	Homerton
10	Emmanuel II
11	Jesus II
12	Pembroke II
13	First and Third II
14	Downing II
15	Sidney Sussex
16	St. Catharine's II
17	St. Edmund's
Division 3
1	Magdalene II
2	Clare II
3	Clare Hall
4	Emmanuel III
5	Peterhouse II
6	Darwin
7	Fitzwilliam II
8	Queens' II
9	Selwyn II
10	Churchill II
11	Jesus III
12	Trinity Hall II
13	Christ's II
14	Robinson II
15	Lucy Cavendish
16	Caius III
17	Lady Margaret III
Division 4
1	Corpus Christi II
2	Wolfson II
3	King's II
4	Girton II
5	Hughes Hall II
6	Pembroke III
7	First and Third III
8	Jesus IV
9	Sidney Sussex II
10	St. Catharine's III
11	Magdalene III
12	Emmanuel IV
13	Churchill III
14	Lucy Cavendish II
15	Clare III
16	Lady Margaret IV
17	Darwin II
Division 5
1	Fitzwilliam III
2	Downing III
3	Selwyn III
4	Peterhouse III
5	Sidney Sussex III
6	First and Third IV
7	Peterhouse IV
8	St. Edmund's II
9	Clare Hall II
10	Trinity Hall III
11	King's III
12	Queens' III
"""
WOMEN_START_ORDER_2025 = """
Division 1
1	Caius
2	Jesus
3	Lady Margaret
4	Emmanuel
5	Trinity Hall
6	Churchill
7	St. Catharine's
8	Newnham
9	Pembroke
10	First and Third
11	Downing
12	Clare
13	Queens'
14	Magdalene
15	Fitzwilliam
16	Sidney Sussex
17	Christ's
Division 2
1	Homerton
2	King's
3	Jesus II
4	Peterhouse
5	Selwyn
6	Girton
7	Lucy Cavendish
8	Wolfson
9	Murray Edwards
10	Newnham II
11	Corpus Christi
12	Emmanuel II
13	Caius II
14	Darwin
15	Hughes Hall
16	Pembroke II
17	Robinson
Division 3
1	Trinity Hall II
2	Lady Margaret II
3	Downing II
4	St. Edmund's
5	Clare II
6	Queens' II
7	Homerton II
8	St. Catharine's II
9	Emmanuel III
10	Caius III
11	Newnham III
12	Murray Edwards II
13	Sidney Sussex II
14	Queens' III
15	Jesus III
16	Lucy Cavendish II
17	Magdalene II
Division 4
1	Pembroke III
2	Clare Hall
3	Clare III
4	Churchill II
5	Christ's II
6	Lady Margaret III
7	First and Third II
8	Fitzwilliam II
9	St. Catharine's III
10	Homerton III
11	King's II
12	Girton II
13	Churchill III
14	Peterhouse II
15	Clare IV
16	Wolfson II
17	Jesus IV
Division 5
1	Corpus Christi II
2	Selwyn II
3	Hughes Hall II
4	Churchill IV
5	Hughes Hall III
6	Murray Edwards III
"""
class Crew:
    def __init__(self, name, start_pos, division):
        self.name = name
        self.start_pos = start_pos
        self.division = division
        self.results = [[0], [0], [0], [0]]
        self.blade_COLOURs = BLADE_COLOURS.get(name, ['#FFFFFF'])
    def reset_results(self):
        self.results = [[0], [0], [0], [0]]

def parse_start_order(order_string):
    crews = []
    current_division = 0
    start_pos_counter = 0
    for line in order_string.strip().split('\n'):
        line = line.strip()
        if not line: continue
        if line.lower().startswith('division'):
            current_division = int(line.split(' ')[1])
            continue
        parts = line.split('\t')
        name = parts[1].strip()
        crews.append(Crew(name, start_pos_counter, current_division))
        start_pos_counter += 1
    return crews

class BumpsSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("May Bumps 2025 Simulator")
        self.configure(bg=BG_COLOUR)
        
        self.men_crews = parse_start_order(MEN_START_ORDER_2025)
        self.women_crews = parse_start_order(WOMEN_START_ORDER_2025)
        self.div_size = 17
        self.current_crews = self.men_crews
        self.positions = []
        self.history = []

        self.current_sex = tk.StringVar(value="Men")
        self.bump_type = tk.IntVar(value=1)

        self.setup_widgets()
        self.update_chart()
        self.save_state_for_undo()

    def setup_widgets(self):
        control_frame = tk.Frame(self, bg=BG_COLOUR)
        control_frame.pack(side="top", fill="x", pady=5, padx=10)
        tk.Label(control_frame, text="Chart:", bg=BG_COLOUR, fg=TEXT_COLOUR).pack(side="left", padx=(0,5))
        ttk.Radiobutton(control_frame, text="Men", variable=self.current_sex, value="Men", command=self.toggle_sex).pack(side="left")
        ttk.Radiobutton(control_frame, text="Women", variable=self.current_sex, value="Women", command=self.toggle_sex).pack(side="left", padx=(0, 20))
        tk.Label(control_frame, text="Click Action:", bg=BG_COLOUR, fg=TEXT_COLOUR).pack(side="left", padx=(20,5))
        ttk.Radiobutton(control_frame, text="Bump", variable=self.bump_type, value=1, command=self.clear_highlight).pack(side="left")
        ttk.Radiobutton(control_frame, text="Overbump", variable=self.bump_type, value=3, command=self.clear_highlight).pack(side="left")
        ttk.Radiobutton(control_frame, text="Double OB", variable=self.bump_type, value=5, command=self.clear_highlight).pack(side="left")
        ttk.Radiobutton(control_frame, text="Triple OB", variable=self.bump_type, value=7, command=self.clear_highlight).pack(side="left")
        ttk.Radiobutton(control_frame, text="Quad OB", variable=self.bump_type, value=9, command=self.clear_highlight).pack(side="left")
        
        undo_button = tk.Button(control_frame, text="Undo", bg="#30363D", fg=TEXT_COLOUR, command=self.undo_last_move, relief="flat", padx=10)
        undo_button.pack(side="right", padx=(5,0))
        reset_button = tk.Button(control_frame, text="Reset All", bg="#30363D", fg=TEXT_COLOUR, command=self.reset_all, relief="flat", padx=10)
        reset_button.pack(side="right")
        
        canvas_frame = tk.Frame(self)
        canvas_frame.pack(side="bottom", fill="both", expand=True)
        self.canvas = tk.Canvas(canvas_frame, bg=BG_COLOUR, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<Motion>", self.handle_hover)
        self.canvas.bind("<Leave>", self.clear_highlight)
        self.canvas.bind("<Configure>", lambda e: self.update_chart())

    def save_state_for_undo(self):
        state = copy.deepcopy([c.results for c in self.current_crews])
        self.history.append(state)

    def undo_last_move(self):
        if len(self.history) > 1:
            self.history.pop()
            last_state = copy.deepcopy(self.history[-1])
            for i, crew in enumerate(self.current_crews):
                crew.results = last_state[i]
            self.update_chart()
            self.clear_highlight()
        else:
            self.reset_all()

    def clear_highlight(self, event=None):
        self.canvas.delete("highlight")

    def toggle_sex(self):
        if self.current_sex.get() == "Men":
            self.current_crews = self.men_crews
        else:
            self.current_crews = self.women_crews
        self.reset_all()

    def reset_all(self):
        for crew in self.current_crews:
            crew.reset_results()
        self.history = [copy.deepcopy([c.results for c in self.current_crews])]
        self.update_chart()

    def calculate_positions(self):
        self.positions = []
        self.positions.append({crew: i for i, crew in enumerate(self.current_crews)})

        for day in range(4):
            start_of_day_order = list(self.positions[day].keys())
            
            intermediate_order = start_of_day_order[:]
            processed_r1 = set()
            for i in range(len(intermediate_order) - 1, -1, -1):
                chaser = intermediate_order[i]
                if chaser in processed_r1: continue
                r1 = chaser.results[day][0] if chaser.results[day] else 0
                if r1 > 0:
                    chased_idx = i - r1
                    if 0 <= chased_idx < len(intermediate_order):
                        chased = intermediate_order[chased_idx]
                        intermediate_order[i], intermediate_order[chased_idx] = chased, chaser
                        processed_r1.add(chaser)
                        processed_r1.add(chased)
            
            final_day_order = intermediate_order[:]
            processed_r2 = set()
            for i in range(len(final_day_order) - 1, -1, -1):
                chaser = final_day_order[i]
                if chaser in processed_r2: continue
                if len(chaser.results[day]) > 1:
                    r2 = chaser.results[day][1]
                    if r2 > 0:
                        chased_idx = i - r2
                        if 0 <= chased_idx < len(final_day_order):
                            chased = final_day_order[chased_idx]
                            final_day_order[i], final_day_order[chased_idx] = chased, chaser
                            processed_r2.add(chaser)
                            processed_r2.add(chased)

            self.positions.append({crew: i for i, crew in enumerate(final_day_order)})

    def draw_chart(self):
        self.canvas.delete("all")
        if not self.positions: return
        total_rows = len(self.current_crews)
        canvas_height = total_rows * ROW_HEIGHT + 100
        canvas_width = self.winfo_width()
        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))
        
        day_width = self.get_day_width()
        if day_width == 0: return

        # Draw Day Labels
        for day in range(4):
            x_center = LEFT_MARGIN + day * day_width + (day_width / 2)
            self.canvas.create_text(x_center, 10, text=f"Day {day+1}", fill=TEXT_COLOUR, font=FONT_DIV)

        for day in range(1, 4):
            x = LEFT_MARGIN + day * day_width
            self.canvas.create_line(x, 20, x, canvas_height, fill=DIVIDER_LINE_COLOUR, dash=(2, 4))
        
        div_boundaries = {}
        last_div = self.current_crews[0].division if self.current_crews else 0
        div_start_index = 0
        for i, crew in enumerate(self.current_crews):
            if crew.division != last_div:
                div_boundaries[last_div] = (div_start_index, i - 1)
                y_pos = (i + 0.5) * ROW_HEIGHT + 20
                self.canvas.create_line(40, y_pos - ROW_HEIGHT / 2, canvas_width, y_pos - ROW_HEIGHT / 2, fill=LINE_COLOUR, dash=(4, 2))
                last_div = crew.division
                div_start_index = i
        div_boundaries[last_div] = (div_start_index, len(self.current_crews) - 1)
        for div_num, (start, end) in div_boundaries.items():
            center_y = ((start + end) / 2 + 0.5) * ROW_HEIGHT + 20
            self.canvas.create_text(20, center_y, text=f"Division {div_num}", fill=TEXT_COLOUR, font=FONT_DIV, anchor="center", angle=90)
        
        start_positions = self.positions[0]
        finish_positions = self.positions[4]
        for crew, start_pos in start_positions.items():
            y_start = (start_pos + 0.5) * ROW_HEIGHT + 20
            self.canvas.create_text(50, y_start, text=f"{start_pos + 1}", fill=TEXT_COLOUR, font=FONT_MAIN, anchor="e")
            self.draw_blade(62, y_start, crew.blade_COLOURs)
            self.canvas.create_text(75, y_start, text=crew.name, fill=TEXT_COLOUR, font=FONT_MAIN, anchor="w")
            
            finish_pos = finish_positions[crew]
            y_finish = (finish_pos + 0.5) * ROW_HEIGHT + 20
            self.canvas.create_text(canvas_width - RIGHT_MARGIN + 8, y_finish, text=crew.name, fill=TEXT_COLOUR, font=FONT_MAIN, anchor="w")
            self.draw_blade(canvas_width - 55, y_finish, crew.blade_COLOURs)
            self.canvas.create_text(canvas_width - 35, y_finish, text=f"{finish_pos + 1}", fill=TEXT_COLOUR, font=FONT_MAIN, anchor="e")
            
            self.draw_crew_line(crew, day_width, LINE_COLOUR, "line")

    def draw_crew_line(self, crew, day_width, COLOUR, tag):
        y_offset = 20
        y_start = (self.positions[0][crew] + 0.5) * ROW_HEIGHT + y_offset
        line_points = [LEFT_MARGIN, y_start]
        for day in range(4):
            pos_before_day = self.positions[day][crew]
            day_results = crew.results[day]
            
            intermediate_pos = pos_before_day - day_results[0]
            
            if len(day_results) > 1:
                x_mid_day = LEFT_MARGIN + day * day_width + (day_width / 2)
                y_mid_day = (intermediate_pos + 0.5) * ROW_HEIGHT + y_offset
                line_points.extend([x_mid_day, y_mid_day])
            
            pos_after_day = self.positions[day+1][crew]
            x_end_day = LEFT_MARGIN + (day + 1) * day_width
            y_end_day = (pos_after_day + 0.5) * ROW_HEIGHT + y_offset
            line_points.extend([x_end_day, y_end_day])
        
        self.canvas.create_line(line_points, fill=COLOUR, width=2.5 if tag == "highlight" else 1.5, tags=tag)

    def draw_blade(self, x, y, COLOURs):
        blade_width, blade_height = 12, 8
        if not COLOURs: COLOURs = ['#FFFFFF']
        num_COLOURs = len(COLOURs)
        stripe_width = blade_width / num_COLOURs
        for i, COLOUR in enumerate(COLOURs):
            x0, y0 = x - blade_width / 2 + i * stripe_width, y - blade_height / 2
            x1, y1 = x - blade_width / 2 + (i + 1) * stripe_width, y + blade_height / 2
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=COLOUR, outline=COLOUR)
    
    def get_day_width(self):
        chart_mid_width = self.winfo_width() - LEFT_MARGIN - RIGHT_MARGIN
        return chart_mid_width / 4 if chart_mid_width > 0 else 0

    def update_chart(self):
        self.calculate_positions()
        self.draw_chart()

    def calculate_intermediate_order(self, day_index):
        day_order = list(self.positions[day_index].keys())
        intermediate_order = day_order[:]
        processed = set()
        for i in range(len(intermediate_order) - 1, -1, -1):
            chaser = intermediate_order[i]
            if chaser in processed: continue
            r1 = chaser.results[day_index][0] if chaser.results[day_index] else 0
            if r1 > 0:
                chased_idx = i - r1
                if 0 <= chased_idx < len(intermediate_order):
                    chased = intermediate_order[chased_idx]
                    intermediate_order[i], intermediate_order[chased_idx] = chased, chaser
                    processed.add(chaser)
                    processed.add(chased)
        return intermediate_order

    def get_interaction_at_coords(self, canvas_x, canvas_y):
        day_width = self.get_day_width()
        if day_width == 0: return None
        
        chart_mid_width = day_width * 4
        if not (LEFT_MARGIN < canvas_x < LEFT_MARGIN + chart_mid_width): return None
        
        day_index = int((canvas_x - LEFT_MARGIN) / day_width)
        clicked_row_index = int((canvas_y - 20) / ROW_HEIGHT)
        bump_val = self.bump_type.get()
        
        day_order = list(self.positions[day_index].keys())
        if not (0 <= clicked_row_index < len(day_order)): return None
        
        potential_chaser = day_order[clicked_row_index]
        
        intermediate_order = self.calculate_intermediate_order(day_index)
        chaser_pos_inter = intermediate_order.index(potential_chaser)
        is_sandwich_for_race2 = chaser_pos_inter != 0 and (chaser_pos_inter + 1) % self.div_size == 1
        
        if is_sandwich_for_race2:
            race_index = 1
            chaser_crew = potential_chaser
            chaser_pos = chaser_pos_inter
            chased_pos = chaser_pos - bump_val
            if chased_pos < 0: return None
            chased_crew = intermediate_order[chased_pos]
            return chaser_crew, chased_crew, race_index, day_index
        else:
            race_index = 0
            chaser_crew = potential_chaser
            chaser_pos_sod = clicked_row_index
            
            chaser_div_pos = (chaser_pos_sod // self.div_size) + 1
            chased_pos = chaser_pos_sod - bump_val
            if chased_pos < 0: return None
            chased_div_pos = (chased_pos // self.div_size) + 1

            if chaser_div_pos != chased_div_pos: return None
            
            chased_crew = day_order[chased_pos]
            return chaser_crew, chased_crew, race_index, day_index

    def handle_hover(self, event):
        self.clear_highlight()
        interaction = self.get_interaction_at_coords(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        if interaction:
            chaser, chased, _, _ = interaction
            day_width = self.get_day_width()
            self.draw_crew_line(chaser, day_width, HIGHLIGHT_COLOUR, "highlight")
            self.draw_crew_line(chased, day_width, HIGHLIGHT_COLOUR, "highlight")

    def process_race1_click(self, day_index, chaser, chased, bump_val):
        day_order = list(self.positions[day_index].keys())
        is_undo = chaser.results[day_index] == [bump_val] or chaser.results[day_index] == [bump_val, 0]
        was_victim_sandwich = day_order.index(chased) != 0 and (day_order.index(chased) + 1) % self.div_size == 1
        
        for crew in day_order:
            if sum(crew.results[day_index]) != 0:
                try:
                    partner_pos = day_order.index(crew) - sum(crew.results[day_index])
                    if 0 <= partner_pos < len(day_order) and (day_order[partner_pos] in [chaser, chased]):
                        crew.results[day_index] = [0]
                except ValueError: pass
        chaser.results[day_index] = [0]
        chased.results[day_index] = [0]

        if not is_undo:
            chaser.results[day_index] = [bump_val, 0] if was_victim_sandwich else [bump_val]
            chased.results[day_index] = [-bump_val]

    def process_race2_click(self, day_index, chaser, chased, bump_val):
        if len(chaser.results[day_index]) == 1:
            chaser.results[day_index].append(0)

        r1 = chaser.results[day_index][0]
        r2 = chaser.results[day_index][1]
        is_undo = r2 == bump_val

        if chased.results[day_index] != [0]:
            chased.results[day_index] = [0]
        
        if is_undo:
            chaser.results[day_index] = [r1, 0]
        else:
            chaser.results[day_index] = [r1, bump_val]
            chased.results[day_index] = [-bump_val]

    def handle_click(self, event):
        interaction = self.get_interaction_at_coords(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        if not interaction: return
        
        self.save_state_for_undo()
        
        chaser_crew, chased_crew, race_index, day_index = interaction
        bump_val = self.bump_type.get()

        if race_index == 0:
            self.process_race1_click(day_index, chaser_crew, chased_crew, bump_val)
        else:
            self.process_race2_click(day_index, chaser_crew, chased_crew, bump_val)
        
        self.update_chart()
        self.handle_hover(event)

if __name__ == "__main__":
    app = BumpsSimulator()
    app.mainloop()