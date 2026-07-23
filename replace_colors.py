import re

def process_file():
    with open('index.html', 'r') as f:
        content = f.read()

    # Define color mappings
    # dark / text / borders -> Crimson Red (#C23032)
    dark_colors = [
        '#130E1C', '#130e1c', '#1a1a1a', '#444', '#555', '#1F152B', '#1f152b', '#2A153A', '#2a153a', 
        '#080512', '#050210', '#0A0818', '#0a0818', '#1A1024', '#1a1024', '#2A1B3B', '#2a1b3b', 
        '#3B1C05', '#3b1c05', '#7A6080', '#7a6080', '#6B5070', '#6b5070', '#9B8BA0', '#9b8ba0', '#000', '#000000'
    ]
    
    # light / background -> Cream (#FFF3E8)
    bg_colors = [
        '#fff', '#ffffff', '#FFF8F0', '#fff8f0', '#fefbf4'
    ]
    
    # accents / gradients -> Gold (#FFD33F)
    accent_colors = [
        '#FFE57F', '#ffe57f', '#FFC107', '#ffc107', '#FFA000', '#ffa000', '#F5A623', '#f5a623', 
        '#FFB81C', '#ffb81c', '#FFE600', '#ffe600', '#B4FF38', '#b4ff38', '#FFE066', '#ffe066', 
        '#FFD54F', '#ffd54f', '#00D4CC', '#00d4cc', '#0ff', '#f00', '#FFF9C4', '#fff9c4', 
        '#E69A38', '#e69a38', '#F5CBA7', '#f5cba7', '#9C4B0F', '#9c4b0f', '#7E5109', '#7e5109', 
        '#B9770E', '#b9770e', '#FDEBD0', '#fdebd0', '#EB984E', '#eb984e', '#A67C00', '#a67c00'
    ]

    for c in dark_colors:
        content = content.replace(c, '#C23032')
        
    for c in bg_colors:
        content = content.replace(c, '#FFF3E8')
        
    for c in accent_colors:
        content = content.replace(c, '#FFD33F')

    # Also replace rgba/rgb
    # Anything like rgba(..., ..., ..., alpha) we can try to leave, or replace.
    # The prompt says: "use this two colours across the website and use the last colour that i decided fro background"
    # To be extremely thorough, let's also update the :root CSS variables so any var(--...) is correct.
    
    with open('index.html', 'w') as f:
        f.write(content)

process_file()
