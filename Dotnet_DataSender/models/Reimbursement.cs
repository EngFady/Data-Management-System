using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text.Json.Serialization;
namespace OracleDataSender.Models
{
    //[Table("ARCAPP_REIMBURSEMENTSEGREG1542", Schema = "c##sharpdj1")]
    [Table("ARCAPP_REIMBURSEMENTSEGREG1542", Schema = "C##SHARPDJ1")]
    public class Reimbursement
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        [Column("ID")]
        public long Id { get; set; }

        [Display(Name = "Box Number")]
        [Range(1, long.MaxValue, ErrorMessage = "You must select a valid box from the list.")]
        [Column("BOX_NUMBER_ID")]
        public long BoxNumberId { get; set; }

        [Display(Name = "Claim Code")]
        [Column("CLAIM_CODE")]
        public string? ClaimCode { get; set; }

        [Display(Name = "Batch Number")]
        [Column("BATCH_NUM")]
        public string? BatchNumber { get; set; }

        // [Display(Name = "Batch Type")]
        // [JsonPropertyName("batch_type")]
        // [Column("BATCH_TYPE")]
        // public string? BatchType  { get; set; }




        [Display(Name = "Batch Type")]
        [Column("BATCH_TYPE")]
        //[JsonPropertyName("batch_type")] // <-- 2. Add this attribute
        public string? BatchType  { get; set; }



        [Display(Name = "English Name")]
        [Column("ENGLISH_NAME")]
        public string? EnglishName { get; set; }

        [Display(Name = "Arabic Name")]
        [Column("ARAB_NAME")]
        public string? ArabicName { get; set; }

        [Display(Name = "Payer")]
        [Column("PAYER")]
        public string? Payer { get; set; }

        [Display(Name = "Policy")]
        [Column("POLICY")]
        public string? Policy { get; set; }

        [Display(Name = "HOF")]
        [Column("HOF")]
        public string? Hof { get; set; }

        [Display(Name = "Audit User")]
        [Column("AUDIT_USER")]
        public string? AuditUser { get; set; }



        [Display(Name = "AUDIT DATE")]
        [Column("AUDIT_DATE")]
        public DateTime AuditDate { get; set; }

        [Column("DATA_ENTRANCE_DATE")]
        public DateTime DataEntranceDate { get; set; }
    }
}