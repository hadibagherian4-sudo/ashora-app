import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';

void main() {
  runApp(const NexaApp());
}

// =====================
// Models (دیتا)
// =====================
class Comment {
  String id;
  String user;
  String text;
  Comment({required this.id, required this.user, required this.text});
}

class Submission {
  String id;
  String title;
  String description;
  String sender;
  String format;
  String field;
  String imgPath;

  /// 'pending', 'waiting_referee', 'correction_needed', 'published'
  String status;

  int score;
  int likes;
  int views;

  String knowledgeCode;
  String refereeFeedback;
  String assignedRefereePhone;

  List<Comment> comments;

  Submission({
    required this.id,
    required this.title,
    required this.description,
    required this.sender,
    required this.format,
    required this.field,
    required this.imgPath,
    this.status = "pending",
    this.score = 0,
    this.likes = 0,
    this.views = 0,
    this.knowledgeCode = "",
    this.refereeFeedback = "",
    this.assignedRefereePhone = "",
    required this.comments,
  });
}

class RefereeProfile {
  String firstName;
  String lastName;
  String phone;
  String nationalId;
  String field;

  RefereeProfile({
    required this.firstName,
    required this.lastName,
    required this.phone,
    required this.nationalId,
    required this.field,
  });
}

// =====================
// Fake DB (حافظه)
// =====================
class FakeDb {
  static List<RefereeProfile> referees = [
    RefereeProfile(
      firstName: "استاد",
      lastName: "نمونه",
      phone: "0912",
      nationalId: "123",
      field: "۲. حوزه فنی و مهندسی",
    ),
  ];

  static List<Submission> submissions = [
    Submission(
      id: "s1",
      title: "بهسازی زیرسازی آزادراه",
      description: "سناریوی اصلاح لایه بیس",
      sender: "واحد مهندسی",
      format: "PDF",
      field: "۱۳. حوزه آسفالت",
      imgPath: "assets/highway_site.jpg",
      status: "published",
      likes: 25,
      views: 500,
      comments: [],
      knowledgeCode: "A-1301",
    ),
    Submission(
      id: "s2",
      title: "اصلاح روش اجرای بتن‌ریزی",
      description: "پیشنهاد بهبود فرآیند ویبره و کیورینگ",
      sender: "کارگاه نمونه",
      format: "DOCX",
      field: "۶. حوزه بتن",
      imgPath: "assets/highway_site.jpg",
      status: "pending",
      likes: 2,
      views: 40,
      comments: [],
    ),
  ];

  static int _id = 100;
  static String nextId() => "s${_id++}";
}

// =====================
// App
// =====================
class NexaApp extends StatelessWidget {
  const NexaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'نکسا (NEXA)',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        scaffoldBackgroundColor: Colors.white,
        primaryColor: const Color(0xFF002d5b),
        fontFamily: 'Tahoma',
        useMaterial3: true,
      ),
      builder: (context, child) => Directionality(
        textDirection: TextDirection.rtl,
        child: child ?? const SizedBox.shrink(),
      ),
      home: const NexaSystemNavigator(),
    );
  }
}

class NexaSystemNavigator extends StatefulWidget {
  const NexaSystemNavigator({super.key});

  @override
  State<NexaSystemNavigator> createState() => _NexaSystemNavigatorState();
}

class _NexaSystemNavigatorState extends State<NexaSystemNavigator> {
  String currentStep = "welcome";
  String userRole = "guest"; // user, manager, referee
  String loginPhone = "";
  String loginId = "";
  int navIdx = 0;

  String loggedInRefereePhone = ""; // برای پنل داور

  final List<String> fieldCommittees = const [
    "۱. حوزه معماری و منظر",
    "۲. حوزه فنی و مهندسی",
    "۳. حوزه برنامه‌ریزی و مدیریت پروژه",
    "۴. حوزه کنترل پروژه",
    "۵. حوزه نقشه‌برداری و فتوگرامتری",
    "۶. حوزه بتن",
    "۷. حوزه هوش مصنوعی",
    "۸. حوزه ICT",
    "۹. حوزه نگهداری و ماشین‌آلات (نت)",
    "۱۰. حوزه کنترل کیفیت (QC)",
    "۱۱. حوزه HSSE",
    "۱۲. حوزه BIM",
    "۱۳. حوزه آسفالت",
    "۱۴. حوزه مالی و حسابداری",
  ];

  final List<String> universityMajors = const [
    "عمران",
    "معماری",
    "مکانیک",
    "برق",
    "هوش مصنوعی",
    "صنایع",
    "مدیریت",
    "حقوق",
  ];

  // پروفایل (دمو)
  final _pName = TextEditingController();
  final _pId = TextEditingController();
  final _pMob = TextEditingController();

  // فرم ارسال محتوا (دمو)
  final _subTitle = TextEditingController();
  final _subDesc = TextEditingController();
  String _selectedField = "۲. حوزه فنی و مهندسی";
  String _pickedFileName = "";

  @override
  void initState() {
    super.initState();
    _selectedField = fieldCommittees.first;
  }

  @override
  void dispose() {
    _pName.dispose();
    _pId.dispose();
    _pMob.dispose();
    _subTitle.dispose();
    _subDesc.dispose();
    super.dispose();
  }

  void _resetApp() => setState(() {
        currentStep = "welcome";
        userRole = "guest";
        navIdx = 0;
        loginPhone = "";
        loginId = "";
        loggedInRefereePhone = "";
      });

  @override
  Widget build(BuildContext context) {
    if (currentStep == "welcome") return _buildWelcome();
    if (currentStep == "login") return _buildLogin();
    if (currentStep == "verify") return _buildVerify();
    return _buildDashboard();
  }

  // =====================
  // UI Pieces
  // =====================
  Widget _appHeader(String sub) => Container(
        width: double.infinity,
        color: const Color(0xFF002d5b),
        padding: const EdgeInsets.only(top: 60, bottom: 25),
        child: Column(
          children: [
            Image.asset(
              "assets/logo.png",
              height: 70,
              errorBuilder: (c, e, s) =>
                  const Icon(Icons.star, color: Colors.white, size: 50),
            ),
            const Text(
              'نکسا (NEXA)',
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 32,
                  fontWeight: FontWeight.w900),
            ),
            const Text('نظام یکپارچه محتوا عاشورا',
                style: TextStyle(color: Colors.white70, fontSize: 10)),
            const SizedBox(height: 10),
            Text(sub, style: const TextStyle(color: Colors.white54, fontSize: 13))
          ],
        ),
      );

  Widget _lbl(String t) => Align(
        alignment: Alignment.centerRight,
        child: Text(
          t,
          style: const TextStyle(
            color: Colors.black,
            fontWeight: FontWeight.bold,
            fontSize: 13,
          ),
        ),
      );

  Widget _primaryBtn(String t, VoidCallback p, {double? width}) => SizedBox(
        width: width ?? double.infinity,
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: const Color(0xFF007bff),
            foregroundColor: Colors.white,
            padding: const EdgeInsets.symmetric(vertical: 16),
          ),
          onPressed: p,
          child: Text(t, style: const TextStyle(fontWeight: FontWeight.bold)),
        ),
      );

  // =====================
  // Auth Flow
  // =====================
  Widget _buildWelcome() => Scaffold(
        body: Column(
          children: [
            _appHeader("ورود به سامانه پایش تخصصی محتوا"),
            Padding(
              padding: const EdgeInsets.all(25),
              child: Column(
                children: [
                  const Text("لطفاً نوع کاربری خود را تعیین کنید:",
                      style: TextStyle(
                          fontWeight: FontWeight.bold, color: Colors.black)),
                  const SizedBox(height: 25),
                  _roleBtn("کاربر عادی (پرسنل اجرایی)", "user"),
                  _roleBtn("داور تخصصی / نخبگان دانشی", "referee"),
                  _roleBtn("مدیر سامانه", "manager"),
                ],
              ),
            )
          ],
        ),
      );

  Widget _roleBtn(String t, String r) => Padding(
        padding: const EdgeInsets.only(bottom: 12),
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.white,
            foregroundColor: Colors.black,
            side: const BorderSide(color: Color(0xFF002d5b), width: 2),
            minimumSize: const Size(double.infinity, 55),
          ),
          onPressed: () => setState(() {
            userRole = r;
            currentStep = "login";
          }),
          child: Text(t, style: const TextStyle(fontWeight: FontWeight.bold)),
        ),
      );

  Widget _buildLogin() => Scaffold(
        body: Padding(
          padding: const EdgeInsets.all(30),
          child: Column(
            children: [
              const SizedBox(height: 80),
              _lbl("شماره همراه فعال سامانه :"),
              TextField(
                onChanged: (v) => loginPhone = v,
                decoration: const InputDecoration(border: OutlineInputBorder()),
              ),
              const SizedBox(height: 15),
              _lbl("کد ملی کاربر (رمز ورود) :"),
              TextField(
                onChanged: (v) => loginId = v,
                obscureText: true,
                decoration: const InputDecoration(border: OutlineInputBorder()),
              ),
              const SizedBox(height: 25),
              _primaryBtn("درخواست کد تایید هویت",
                  () => setState(() => currentStep = "verify"))
            ],
          ),
        ),
      );

  Widget _buildVerify() => Scaffold(
        body: Center(
          child: _primaryBtn("تایید و ورود نهایی", _handleFinalLogin, width: 250),
        ),
      );

  void _handleFinalLogin() {
    if (userRole == "referee") {
      final ok = FakeDb.referees.any((r) =>
          r.phone.trim() == loginPhone.trim() &&
          r.nationalId.trim() == loginId.trim());
      if (!ok) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text("هویت داوری شما توسط مدیر ثبت نشده است")),
        );
        return;
      }
      loggedInRefereePhone = loginPhone.trim();
    }
    setState(() => currentStep = "main");
  }

  // =====================
  // Dashboard
  // =====================
  Widget _buildDashboard() {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "نکسا | میز $userRole",
          style: const TextStyle(
            color: Color(0xFF002d5b),
            fontWeight: FontWeight.bold,
            fontSize: 14,
          ),
        ),
        actions: [
          IconButton(
              onPressed: _resetApp,
              icon: const Icon(Icons.logout, color: Colors.red))
        ],
      ),
      body: _buildPage(),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: navIdx,
        selectedItemColor: const Color(0xFF002d5b),
        onTap: (i) => setState(() => navIdx = i),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: "میز کار"),
          BottomNavigationBarItem(
              icon: Icon(Icons.forum_outlined), label: "تالار گفتگو"),
          BottomNavigationBarItem(icon: Icon(Icons.person_pin), label: "پروفایل"),
        ],
      ),
    );
  }

  Widget _buildPage() {
    if (navIdx == 1) return _buildChatForum();
    if (navIdx == 2) return _buildProfileEditor();

    if (userRole == "user") return _buildUserWorkbench();
    if (userRole == "manager") return _buildManagerWorkbench();
    return _buildRefereeWorkbench();
  }

  // =====================
  // USER Workbench
  // =====================
  Widget _buildUserWorkbench() => DefaultTabController(
        length: 4,
        child: Column(
          children: [
            const TabBar(
              isScrollable: true,
              labelColor: Color(0xFF002d5b),
              indicatorColor: Color(0xFFfbbf24),
              tabs: [
                Tab(text: "ویترین دانش"),
                Tab(text: "ارسال محتوا"),
                Tab(text: "وضعیت پیگیری"),
                Tab(text: "پیشنهاد موضوعات"),
              ],
            ),
            Expanded(
              child: TabBarView(
                children: [
                  _buildShowcase(),
                  _buildSubmitForm(),
                  _buildTracking(),
                  _buildUniversityList(),
                ],
              ),
            )
          ],
        ),
      );

  Widget _buildShowcase() => ListView.builder(
        itemCount: FakeDb.submissions.length,
        itemBuilder: (c, i) => _buildContentCard(FakeDb.submissions[i]),
      );

  Widget _buildContentCard(Submission s) => Card(
        margin: const EdgeInsets.all(15),
        clipBehavior: Clip.antiAlias,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15),
          side: BorderSide(color: Colors.grey.shade200),
        ),
        child: Column(
          children: [
            Image.asset(
              s.imgPath,
              height: 180,
              width: double.infinity,
              fit: BoxFit.cover,
              errorBuilder: (c, e, st) => Container(
                height: 180,
                color: Colors.blue.shade50,
                child: const Icon(Icons.engineering),
              ),
            ),
            ListTile(
              title: Text(
                s.title,
                style: const TextStyle(
                    fontWeight: FontWeight.bold, color: Colors.black),
              ),
              subtitle: Text("${s.field} | وضعیت: ${_statusFa(s.status)}"),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10),
              child: Row(
                children: [
                  IconButton(
                    icon: const Icon(Icons.favorite_border, color: Colors.red),
                    onPressed: () => setState(() => s.likes++),
                  ),
                  Text(" پسندیدن (${s.likes})",
                      style: const TextStyle(
                          fontWeight: FontWeight.bold, fontSize: 11)),
                  const Spacer(),
                  TextButton(
                    onPressed: () => _openComments(s),
                    child: const Text("نظرات",
                        style: TextStyle(fontWeight: FontWeight.bold)),
                  )
                ],
              ),
            )
          ],
        ),
      );

  void _openComments(Submission s) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      builder: (c) => Padding(
        padding: EdgeInsets.only(
          bottom: MediaQuery.of(c).viewInsets.bottom,
          top: 15,
          left: 15,
          right: 15,
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text("بخش تبادل دیدگاه‌های تخصصی",
                style: TextStyle(fontWeight: FontWeight.bold)),
            SizedBox(
              height: 200,
              child: ListView.builder(
                itemCount: s.comments.length,
                itemBuilder: (cc, ii) => ListTile(
                  title: Text(
                    s.comments[ii].user,
                    style: const TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: Colors.blueGrey,
                    ),
                  ),
                  subtitle: Text(s.comments[ii].text,
                      style: const TextStyle(color: Colors.black)),
                  trailing: userRole == "manager"
                      ? IconButton(
                          icon: const Icon(Icons.delete, color: Colors.red),
                          onPressed: () {
                            setState(() => s.comments.removeAt(ii));
                            Navigator.pop(c);
                          },
                        )
                      : null,
                ),
              ),
            ),
            TextField(
              decoration: const InputDecoration(
                hintText: "درج دیدگاه...",
                border: OutlineInputBorder(),
              ),
              onSubmitted: (v) {
                if (v.trim().isEmpty) return;
                setState(() {
                  s.comments.add(
                      Comment(id: "c${DateTime.now().millisecondsSinceEpoch}", user: "کاربر", text: v));
                });
                Navigator.pop(c);
              },
            ),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  Widget _buildSubmitForm() => SingleChildScrollView(
        padding: const EdgeInsets.all(25),
        child: Column(
          children: [
            TextField(
              controller: _subTitle,
              decoration: const InputDecoration(
                labelText: "عنوان سناریو / محتوای فنی",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: _subDesc,
              maxLines: 3,
              decoration: const InputDecoration(
                labelText: "توضیحات",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            DropdownButtonFormField<String>(
              decoration: const InputDecoration(
                labelText: "حوزه تخصصی پیشنهادی",
                border: OutlineInputBorder(),
              ),
              value: _selectedField,
              items: fieldCommittees
                  .map((e) => DropdownMenuItem(value: e, child: Text(e)))
                  .toList(),
              onChanged: (v) => setState(() => _selectedField = v ?? _selectedField),
            ),
            const SizedBox(height: 15),
            _filePickerField(),
            const SizedBox(height: 10),
            Align(
              alignment: Alignment.centerRight,
              child: Text(
                _pickedFileName.isEmpty ? "فایلی انتخاب نشده" : "فایل: $_pickedFileName",
                style: const TextStyle(fontSize: 12, color: Colors.black54),
              ),
            ),
            const SizedBox(height: 20),
            _primaryBtn("ثبت نهایی و ارسال به سازمان", _submitNewContent),
          ],
        ),
      );

  Widget _filePickerField() => InkWell(
        onTap: () async {
          final res = await FilePicker.platform.pickFiles();
          if (res != null && res.files.isNotEmpty) {
            setState(() => _pickedFileName = res.files.first.name);
            if (mounted) {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text("فایل با موفقیت انتخاب شد.")),
              );
            }
          }
        },
        child: Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            border: Border.all(color: Colors.grey),
            borderRadius: BorderRadius.circular(10),
            color: Colors.grey.shade50,
          ),
          child: const Row(
            children: [
              Icon(Icons.attachment),
              SizedBox(width: 15),
              Text("پیوست فایل (حافظه گوشی یا رایانه)"),
            ],
          ),
        ),
      );

  void _submitNewContent() {
    if (_subTitle.text.trim().isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("عنوان را وارد کنید")),
      );
      return;
    }

    final s = Submission(
      id: FakeDb.nextId(),
      title: _subTitle.text.trim(),
      description: _subDesc.text.trim(),
      sender: "کاربر",
      format: _pickedFileName.isEmpty ? "N/A" : _pickedFileName,
      field: _selectedField,
      imgPath: "assets/highway_site.jpg",
      status: "pending",
      comments: [],
    );

    setState(() {
      FakeDb.submissions.insert(0, s);
      _subTitle.clear();
      _subDesc.clear();
      _pickedFileName = "";
    });

    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text("با موفقیت ثبت شد و در صف بررسی قرار گرفت ✅")),
    );
  }

  Widget _buildTracking() {
    final my = FakeDb.submissions.where((s) => s.sender == "کاربر").toList();
    if (my.isEmpty) {
      return const Center(child: Text("هنوز چیزی ارسال نکردی."));
    }
    return ListView.builder(
      itemCount: my.length,
      itemBuilder: (c, i) => ListTile(
        title: Text(my[i].title),
        subtitle: Text("وضعیت: ${_statusFa(my[i].status)}"),
        trailing: const Icon(Icons.timer),
      ),
    );
  }

  Widget _buildUniversityList() => ListView.builder(
        itemCount: universityMajors.length,
        itemBuilder: (c, i) => Card(
          child: ListTile(
            title: Text("رشته ${universityMajors[i]}"),
            subtitle: const Text("پیشنهاد موضوعات خدمت و پایان‌نامه"),
          ),
        ),
      );

  // =====================
  // MANAGER Workbench
  // =====================
  Widget _buildManagerWorkbench() => DefaultTabController(
        length: 2,
        child: Column(
          children: [
            const TabBar(
              labelColor: Color(0xFF002d5b),
              tabs: [
                Tab(text: "میز ارجاع ارشد"),
                Tab(text: "ثبت داور تخصصی"),
              ],
            ),
            Expanded(
              child: TabBarView(
                children: [
                  _buildManagerReferralDesk(),
                  _addRefereeForm(),
                ],
              ),
            )
          ],
        ),
      );

  Widget _buildManagerReferralDesk() {
    final pending = FakeDb.submissions.where((s) => s.status == "pending").toList();
    if (pending.isEmpty) {
      return const Center(child: Text("موردی برای ارجاع وجود ندارد."));
    }

    return ListView.builder(
      itemCount: pending.length,
      itemBuilder: (c, i) {
        final s = pending[i];
        return ListTile(
          title: Text(s.title),
          subtitle: Text("فرستنده: ${s.sender} | حوزه: ${s.field}"),
          trailing: ElevatedButton(
            onPressed: () => _showReferralDialog(s),
            child: const Text("بررسی و ارجاع"),
          ),
        );
      },
    );
  }

  void _showReferralDialog(Submission sub) {
    RefereeProfile? selected = FakeDb.referees.isNotEmpty ? FakeDb.referees.first : null;

    showDialog(
      context: context,
      builder: (c) => AlertDialog(
        title: const Text("ارجاع به داور:"),
        content: DropdownButton<RefereeProfile>(
          isExpanded: true,
          value: selected,
          items: FakeDb.referees
              .map((r) => DropdownMenuItem(
                    value: r,
                    child: Text("${r.firstName} ${r.lastName} - ${r.field}"),
                  ))
              .toList(),
          onChanged: (v) => selected = v,
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(c),
            child: const Text("لغو"),
          ),
          ElevatedButton(
            onPressed: () {
              if (selected == null) return;
              setState(() {
                sub.status = "waiting_referee";
                sub.assignedRefereePhone = selected!.phone;
              });
              Navigator.pop(c);
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text("ارجاع انجام شد ✅")),
              );
            },
            child: const Text("ارجاع"),
          )
        ],
      ),
    );
  }

  Widget _addRefereeForm() => SingleChildScrollView(
        padding: const EdgeInsets.all(25),
        child: Column(
          children: [
            const Text("تعریف داور فنی (صدور اجازه ورود)",
                style: TextStyle(fontWeight: FontWeight.bold)),
            const SizedBox(height: 15),
            TextField(
              decoration: const InputDecoration(
                labelText: "نام",
                border: OutlineInputBorder(),
              ),
              onChanged: (v) => _tmpRefFirst = v,
            ),
            const SizedBox(height: 10),
            TextField(
              decoration: const InputDecoration(
                labelText: "نام خانوادگی",
                border: OutlineInputBorder(),
              ),
              onChanged: (v) => _tmpRefLast = v,
            ),
            const SizedBox(height: 10),
            TextField(
              decoration: const InputDecoration(
                labelText: "شماره همراه",
                border: OutlineInputBorder(),
              ),
              onChanged: (v) => _tmpRefPhone = v,
            ),
            const SizedBox(height: 10),
            TextField(
              decoration: const InputDecoration(
                labelText: "کد ملی (ID ورود)",
                border: OutlineInputBorder(),
              ),
              onChanged: (v) => _tmpRefNid = v,
            ),
            const SizedBox(height: 10),
            DropdownButtonFormField<String>(
              decoration: const InputDecoration(
                labelText: "حوزه تخصصی",
                border: OutlineInputBorder(),
              ),
              value: _tmpRefField,
              items: fieldCommittees
                  .map((e) => DropdownMenuItem(value: e, child: Text(e)))
                  .toList(),
              onChanged: (v) => setState(() => _tmpRefField = v ?? _tmpRefField),
            ),
            const SizedBox(height: 20),
            _primaryBtn("تایید و ساخت پنل نخبگان", _saveReferee),
          ],
        ),
      );

  String _tmpRefFirst = "";
  String _tmpRefLast = "";
  String _tmpRefPhone = "";
  String _tmpRefNid = "";
  String _tmpRefField = "۲. حوزه فنی و مهندسی";

  void _saveReferee() {
    if (_tmpRefPhone.trim().isEmpty || _tmpRefNid.trim().isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("شماره همراه و کد ملی الزامی است")),
      );
      return;
    }
    setState(() {
      FakeDb.referees.add(
        RefereeProfile(
          firstName: _tmpRefFirst.trim().isEmpty ? "داور" : _tmpRefFirst.trim(),
          lastName: _tmpRefLast.trim().isEmpty ? "جدید" : _tmpRefLast.trim(),
          phone: _tmpRefPhone.trim(),
          nationalId: _tmpRefNid.trim(),
          field: _tmpRefField,
        ),
      );
      _tmpRefFirst = "";
      _tmpRefLast = "";
      _tmpRefPhone = "";
      _tmpRefNid = "";
      _tmpRefField = fieldCommittees.first;
    });

    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text("داور جدید با موفقیت ثبت شد ✅")),
    );
  }

  // =====================
  // REFEREE Workbench
  // =====================
  Widget _buildRefereeWorkbench() => DefaultTabController(
        length: 2,
        child: Column(
          children: [
            const TabBar(
              labelColor: Color(0xFF002d5b),
              tabs: [
                Tab(text: "ارجاع‌شده به من"),
                Tab(text: "بازخورد / نتیجه"),
              ],
            ),
            Expanded(
              child: TabBarView(
                children: [
                  _buildRefereeInbox(),
                  _buildRefereeActions(),
                ],
              ),
            )
          ],
        ),
      );

  Submission? _selectedForReferee;

  Widget _buildRefereeInbox() {
    final mine = FakeDb.submissions
        .where((s) => s.assignedRefereePhone == loggedInRefereePhone)
        .toList();

    if (mine.isEmpty) {
      return const Center(
        child: Text("فعلاً چیزی به شما ارجاع نشده."),
      );
    }

    return ListView.builder(
      itemCount: mine.length,
      itemBuilder: (c, i) => ListTile(
        title: Text(mine[i].title),
        subtitle: Text("وضعیت: ${_statusFa(mine[i].status)}"),
        trailing: ElevatedButton(
          onPressed: () => setState(() => _selectedForReferee = mine[i]),
          child: const Text("انتخاب"),
        ),
      ),
    );
  }

  final _refFeedbackCtrl = TextEditingController();

  Widget _buildRefereeActions() {
    final s = _selectedForReferee;
    if (s == null) {
      return const Center(child: Text("یک مورد را از تب «ارجاع‌شده به من» انتخاب کن."));
    }

    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        children: [
          Text("عنوان: ${s.title}", style: const TextStyle(fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          Align(
              alignment: Alignment.centerRight,
              child: Text("توضیحات: ${s.description}")),
          const SizedBox(height: 12),
          DropdownButtonFormField<String>(
            decoration: const InputDecoration(
              labelText: "نتیجه بررسی",
              border: OutlineInputBorder(),
            ),
            value: s.status,
            items: const [
              DropdownMenuItem(value: "waiting_referee", child: Text("در حال بررسی")),
              DropdownMenuItem(value: "correction_needed", child: Text("نیاز به اصلاح")),
              DropdownMenuItem(value: "published", child: Text("تایید و انتشار")),
            ],
            onChanged: (v) {
              if (v == null) return;
              setState(() => s.status = v);
            },
          ),
          const SizedBox(height: 12),
          TextField(
            controller: _refFeedbackCtrl..text = s.refereeFeedback,
            maxLines: 4,
            decoration: const InputDecoration(
              labelText: "بازخورد داور",
              border: OutlineInputBorder(),
            ),
            onChanged: (v) => s.refereeFeedback = v,
          ),
          const SizedBox(height: 12),
          TextField(
            decoration: const InputDecoration(
              labelText: "کد دانشی (اختیاری)",
              border: OutlineInputBorder(),
            ),
            onChanged: (v) => s.knowledgeCode = v,
          ),
          const SizedBox(height: 16),
          _primaryBtn("ثبت نتیجه", () {
            setState(() {});
            ScaffoldMessenger.of(context).showSnackBar(
              const SnackBar(content: Text("نتیجه ثبت شد ✅")),
            );
          }),
        ],
      ),
    );
  }

  // =====================
  // Chat + Profile
  // =====================
  Widget _buildChatForum() => Column(
        children: [
          const Expanded(
            child: Center(
              child: Text(
                "🗨️ تالار گفتگو سراسری نکسا\n"
                "(چت عمومی دمو است)",
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.black),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(15),
            child: TextField(
              decoration: const InputDecoration(
                hintText: "درج پیام...",
                suffixIcon: Icon(Icons.send, color: Colors.blue),
                border: OutlineInputBorder(),
              ),
              onSubmitted: (v) {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text("پیام ارسال شد (دمو)")),
                );
              },
            ),
          ),
          const SizedBox(height: 50)
        ],
      );

  Widget _buildProfileEditor() => SingleChildScrollView(
        padding: const EdgeInsets.all(25),
        child: Column(
          children: [
            const CircleAvatar(
              radius: 50,
              backgroundColor: Color(0xFF002d5b),
              child: Icon(Icons.person, color: Colors.white, size: 50),
            ),
            const SizedBox(height: 25),
            TextField(
              controller: _pName,
              decoration: const InputDecoration(
                labelText: "نام و نام خانوادگی",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: _pId,
              decoration: const InputDecoration(
                labelText: "کد ملی شخصی",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: _pMob,
              decoration: const InputDecoration(
                labelText: "شماره همراه سازمانی",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 30),
            _primaryBtn("ذخیره نهایی اطلاعات", () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text("ذخیره شد (دمو)")),
              );
            })
          ],
        ),
      );

  // =====================
  // Helpers
  // =====================
  String _statusFa(String s) {
    switch (s) {
      case "pending":
        return "در انتظار ارجاع";
      case "waiting_referee":
        return "در انتظار نظر داور";
      case "correction_needed":
        return "نیاز به اصلاح";
      case "published":
        return "منتشر شده";
      default:
        return s;
    }
  }
}
