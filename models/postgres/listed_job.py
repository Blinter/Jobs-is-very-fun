"""
DB Models
Postgres
Listed Job Table
"""
from sqlalchemy.dialects.postgresql import TSVECTOR

from extensions_sql import db
from models.postgres.company import Company
from sqlalchemy.orm.attributes import flag_modified


class ListedJob(db.Model):
    """
    Main Object used by website for filtering and providing data to the user.
    """
    __bind_key__ = "postgres"

    __tablename__ = "listed_jobs"

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.VARCHAR,
        nullable=False
    )

    description = db.Column(
        db.TEXT(),
        nullable=True
    )

    search_vector_name = db.Column(
        TSVECTOR
    )

    search_vector_description = db.Column(
        TSVECTOR
    )

    search_vector = db.Column(
        TSVECTOR
    )

    salary_currency = db.Column(
        db.VARCHAR,
        nullable=True
    )

    min_salary = db.Column(
        db.Integer,
        nullable=True
    )

    max_salary = db.Column(
        db.Integer,
        nullable=True
    )

    apply_link = db.Column(
        db.Text(),
        nullable=False
    )

    original_source_link = db.Column(
        db.Text(),
        nullable=True
    )

    posted_time_utc = db.Column(
        db.DateTime(timezone=False),
        nullable=True
    )

    expiration_time_utc = db.Column(
        db.DateTime(timezone=False),
        nullable=True
    )

    company_id = db.Column(
        db.Integer,
        db.ForeignKey('companies.id'),
        nullable=True
    )

    company = db.relationship(
        'Company',
        back_populates="listed_jobs",
        lazy='select',
        viewonly=True
    )

    api_source_id = db.Column(
        db.Integer,
        db.ForeignKey('api_sources.id'),
        nullable=False
    )

    api_source = db.relationship(
        'APISource',
        back_populates="listed_jobs",
        lazy='select',
        viewonly=True
    )

    api_reference_name = db.Column(
        db.VARCHAR,
        nullable=False
    )

    listed_job_job_types = db.relationship(
        'ListedJobJobType',
        back_populates="listed_job",
        cascade="all, delete",
        lazy='select'
    )

    listed_job_experience_levels = db.relationship(
        'ListedJobExperienceLevel',
        back_populates="listed_job",
        cascade="all, delete",
        lazy='select'
    )

    listed_job_location = db.relationship(
        'ListedJobLocation',
        back_populates="listed_job",
        cascade="all, delete",
        lazy='select'
    )

    saved_jobs = db.relationship(
        'SavedJob',
        back_populates="listed_job",
        cascade="all, delete",
        lazy='select',
        viewonly=True
    )

    def __repr__(self):
        """Show info about Job Type."""

        return ("<ListedJob "
                f"id={str(self.id)} "
                f"name={str(self.name)} " +

                # (f"salary_currency={str(self.salary_currency)} "
                #  if (self.salary_currency is not None and
                #      len(str(self.salary_currency)) != 0) else '') +

                # (f"min_salary={str(self.min_salary)} "
                #  if (self.min_salary is not None and
                #      len(str(self.min_salary)) != 0) else '') +

                # (f"max_salary={str(self.max_salary)} "
                #  if (self.max_salary is not None and
                #      len(str(self.max_salary)) != 0) else '') +

                # (f"apply_link={str(self.apply_link)} "
                #  if (self.apply_link is not None and
                #      len(str(self.apply_link)) != 0) else '') +

                # (f"original_source_link={str(self.original_source_link)} "
                #  if (self.original_source_link is not None and
                #      len(str(self.original_source_link)) != 0) else '') +

                # (f"posted_time_utc={str(self.posted_time_utc)} "
                #  if (self.posted_time_utc is not None and
                #      len(str(self.posted_time_utc)) != 0) else '') +

                # (f"expiration_time_utc={str(self.expiration_time_utc)} "
                #  if (self.expiration_time_utc is not None and
                #      len(str(self.expiration_time_utc)) != 0) else '') +

                # (f"api_source={str(self.api_source)} "
                #  if self.api_source_id is not None else '') +

                # ((("[trunc.] " if len(str(self.description)) > 64 else "") +
                #   f"name={str(self.description)[:64]} "
                #   if len(str(self.description)) != 0 else '')
                #  if self.description is not None else '') +

                ("company_id="
                 f"{str(self.company_id)} "
                 if self.company_id is not None else '') +

                # ((("[trunc.] "
                #    if len(str(self.listed_job_job_types)) > 16 else "") +
                #   "listed_job_job_types="
                #   f"{str(self.listed_job_job_types)[:16]} "
                #   if len(str(self.listed_job_job_types)) != 0 else '')
                #  if self.listed_job_job_types is not None else '') +

                # ((("[trunc.] "
                #    if len(str(self.listed_job_experience_levels)) > 16
                #    else "") +
                #   "listed_job_experience_levels="
                #   f"{str(self.listed_job_experience_levels)[:16]} "
                #   if len(str(self.listed_job_experience_levels))
                #   != 0
                #   else '')
                #  if self.listed_job_experience_levels is not None else '') +
                #
                # ((("[trunc.] "
                #    if len(str(self.listed_job_location)) > 24 else "") +
                #   "listed_job_location=" +
                #   f"{str(self.listed_job_location)[:24]} "
                #   if len(str(self.listed_job_location)) != 0 else '')
                #  if self.listed_job_location is not None else '') +

                ">")

    def to_dict_rest(self):
        """
        Convert a ListedJob into a dictionary which is then sent to the client.
        """
        return {
            'id': self.id,
            'name': self.name,

            'company': self.company.name
            if self.company_id is not None else None,

            'salary_currency': self.salary_currency
            if (self.salary_currency is not None and
                (isinstance(self.min_salary, int) and
                 self.min_salary > 0) or
                (isinstance(self.max_salary, int) and
                 self.max_salary > 0))
            else None,

            'min_salary': self.min_salary
            if (self.salary_currency is not None and
                self.min_salary is not None and
                isinstance(self.salary_currency, str) and
                isinstance(self.min_salary, int) and
                self.min_salary > 0)
            else None,

            'max_salary': self.max_salary
            if (self.salary_currency is not None and
                self.max_salary is not None and
                self.min_salary is not None and
                isinstance(self.salary_currency, str) and
                isinstance(self.max_salary, int) and
                isinstance(self.min_salary, int) and
                self.min_salary > 0)
            else None,

            'location': (
                self.listed_job_location[0]
                .listed_job_location.to_jobs_rest())
            if (self.listed_job_location is not None and
                len(self.listed_job_location) >= 1)
            else None,

            'job_type': (
                self.listed_job_experience_levels[0].experience_level.name)
            if (self.listed_job_experience_levels is not None and
                len(self.listed_job_experience_levels) >= 1)
            else '',

            # 'No Experience Level defined',
            'description': (
                self.description[:100] + "..."
                if len(self.description) > 100 else self.description)
            if (self.description is not None and
                self.description != '')
            else 'No Description',

            'posted_time_utc': self.posted_time_utc,

            'api_source': self.api_source.name[
                self.api_source.name.find("|") + 1:].strip(),
        }

    @db.orm.declared_attr
    def __table_args__(self):
        return (

            # BST
            db.Index(
                'idx_listed_job_posted_time_utc',
                self.posted_time_utc,
            ),

            # BST
            db.Index(
                'idx_listed_job_expiration_time_utc',
                self.expiration_time_utc,
            ),

            # BST
            db.Index(
                'idx_listed_job_min_salary',
                self.min_salary,
            ),

            # BST
            db.Index(
                'idx_listed_job_max_salary',
                self.max_salary,
            ),

            # BST
            db.Index(
                'idx_listed_job_salary_currency',
                self.salary_currency,
                postgresql_using='hash'
            ),

            # Hash
            db.Index(
                'idx_listed_job_company_id',
                self.company_id,
                postgresql_using='hash'
            ),

            # Hash
            db.Index(
                'idx_listed_job_api_source_id',
                self.api_source_id,
                postgresql_using='hash'
            ),

            # Generalized Inverted Index
            db.Index(
                'idx_listed_job_search_vector_name',
                self.search_vector_name,
                postgresql_using='gin'
            ),

            # Generalized Inverted Index
            db.Index(
                'idx_listed_job_search_vector_description',
                self.search_vector_description,
                postgresql_using='gin'
            ),

            # Generalized Inverted Index
            db.Index(
                'idx_listed_job_search_vector',
                self.search_vector,
                postgresql_using='gin'
            ),

            # Name Only
            # Trigram Name Only
            # Generalized Inverted Index
            db.Index(
                'idx_listed_job_name_trgm',
                self.name,
                postgresql_using='gin',
                postgresql_ops={
                    'name': 'gin_trgm_ops'
                }
            ),

            # Description Only
            # Trigram
            # Generalized Inverted Index
            db.Index(
                'idx_listed_job_description_trgm',
                self.description,
                postgresql_using='gin',
                postgresql_ops={
                    'description': 'gin_trgm_ops'
                }
            ),

            # Name and Description (Combined)
            # Trigram Name
            # Generalized Inverted Index
            db.Index(
                'idx_listed_job_trgm',
                db.text("(name || ' ' || description) gin_trgm_ops"),
                postgresql_using='gin'
            ),
        )


@db.event.listens_for(ListedJob, 'before_insert')
@db.event.listens_for(ListedJob, 'before_update')
def update_listed_job_search_vector(_, __, target):
    """
    Update search vectors
    Additional logic to check that the values being inserted are not tuples.
    """
    name_changed = db.inspect(target).attrs.name.history.has_changes()
    if name_changed:
        target.name = (
            target.name[0]
            if isinstance(target.name, tuple) else str(target.name)
            if target.name else ''
        )
        target.search_vector_name = db.func.to_tsvector(target.name)
        flag_modified(target, "search_vector_name")

    description_changed = (
        db.inspect(target).attrs.description.history.has_changes())
    if description_changed:
        target.description = (
            target.description[0]
            if isinstance(target.description, tuple)
            else str(target.description)
            if target.description else ''
        )
        target.search_vector_description = db.func.to_tsvector(
            target.description)
        flag_modified(target, "search_vector_description")

    if (name_changed or
            description_changed):
        target.search_vector = db.func.to_tsvector(
            ' '.join(filter(None, [
                target.name,
                target.description
            ]))
        )
        flag_modified(target, "search_vector")


update_count_function_ddl = db.DDL(f"""\
CREATE OR REPLACE FUNCTION update_listed_job_count() RETURNS TRIGGER AS $$
BEGIN
    UPDATE {Company.__tablename__}
    SET listed_job_count = (
        SELECT COUNT(*)
        FROM {ListedJob.__tablename__}
        WHERE {ListedJob.__tablename__}.company_id = NEW.company_id
    )
    WHERE {Company.__tablename__}.id = NEW.company_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;\
""")

update_count_trigger_ddl = db.DDL(f"""\
CREATE TRIGGER listed_job_count_trigger
AFTER INSERT OR DELETE OR UPDATE ON listed_jobs
FOR EACH ROW
EXECUTE FUNCTION update_listed_job_count();\
""")

db.event.listen(ListedJob.__table__, 'after_create', update_count_function_ddl)
db.event.listen(ListedJob.__table__, 'after_create', update_count_trigger_ddl)
