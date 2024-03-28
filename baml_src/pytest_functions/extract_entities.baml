enum TimePeriod {
    ANCIENT
    MEDIEVAL
    RENAISSANCE
    MODERN
}

enum MaterialOrigin {
    NATURAL
    SYNTHETIC
}

enum ManuscriptState {
    INITIAL
    RESTORED
}

class ManuscriptContext {
    timePeriod TimePeriod
    origin string?  // Ambiguous: Could refer to geographic location or cultural origin
    importance string?  // Vague description requiring inference on significance
}

class Restoration {
    baseMaterials MaterialOrigin[]
    inkAndBindMaterials string[]  // Vague: Requires mapping to specific types or origins
    additionalTechniques string[]  // Ambiguous: Could include both preservation and repair techniques
}

class ManuscriptCondition {
    initialState ManuscriptState  // Vague: Based on loose descriptions rather than detailed assessment
    finalState ManuscriptState  // Requires interpretation of described improvements or remaining issues
    actionsTaken string[]  // Ambiguous: General actions without specifying exact processes
    unresolvedIssues string[]  // Vague: Mentioned issues without clear identification
}

class ComplexRestorationProject {
    id string
    title string  // Ambiguity in identifying the manuscript
    context ManuscriptContext
    materials Restoration
    condition ManuscriptCondition
    actionsTaken string[]  // Ambiguous: General actions without specifying exact processes
    unresolvedIssues string[]  // Vague: Mentioned issues without clear identification
    isComplete bool  // Ambiguity in what constitutes 'completion'
}

function AnalyzeRestorationProject {
  input string
  output ComplexRestorationProject
}

impl<llm, AnalyzeRestorationProject> v1 {
  client GPT4
  prompt #"
    Given the following restoration project document, analyze the details and provide the following information in json schema format:

    Document:
    ---
    {#input}
    ---


    Use these enum definitions:
    {#print_enum(TimePeriod)}
    ---

    {#print_enum(MaterialOrigin)}
    ---

    {#print_enum(ManuscriptState)}
    ---

    Answer in this JSON format:
    {#print_type(output)}

    JSON:
  "#
}